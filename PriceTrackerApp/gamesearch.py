import urllib
import requests
import bs4
import json
import os

from googlesearch import search
from bs4 import BeautifulSoup

#Import specific vendor scrapers
from PriceTrackerApp.scrapersAndAPIs import amznScraper, nintendoScraper, steamAPI, xboxScraper, psScraper

#Returns list of links with their associated vendor name for a game specified
def searchGame(query):
    #query should include 'buy', 'purchase', etc. at the end to bring up most useful results
    query = query + " buy"
    links = []
    for i in search(query, tld="co.in", num=15, stop=15, pause=3):
        site = i.split(".")

        #list of vendors we know how to scrape info from
        vendors = ["steampowered", "xbox", "amazon", "nintendo", "playstation"]
        for j in vendors:
            if site[1] == j:
                soup = BeautifulSoup(requests.get(i).text, 'html.parser') 
                title = (soup.find_all('title')[0].get_text()).lower()

                #Often empty search results for sites will come up
                #as well as soundtracks and expansions for the game - remove them
                banned_keywords = ["search", "recommended", "soundtrack", "expansion", "dlc"]
                if (all(i not in title for i in banned_keywords)):
                    links.append((i, site[1]))

    return links

#Given list of links with their associated website name, scrape info using appropriate scraper and return game dict
def scrapeGame(links):
    gameList = []
    for url, vendor in links:
        #Simulate user - otherwise sites like amazon will block
        headers = headers = { 
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36', 
        'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 
        'Accept-Language' : 'en-US,en;q=0.5',
        'Accept-Encoding' : 'gzip', 
        'DNT' : '1', # Do Not Track Request Header 
        'Connection' : 'close'
        }
        page = requests.get(url, headers=headers)
        soup  = bs4.BeautifulSoup(page.content, "html.parser")
        parsed_url = urllib.parse.urlparse(url)
        vendorHost = parsed_url.netloc.strip()
        if vendor == "amazon":
            title = amznScraper.get_title(soup)
            price = amznScraper.get_price(soup)
            platform = amznScraper.get_platform(soup)

            #Remove scrap from platform
            if platform != "":
                platform = platform.split(':')[1]
                platform = platform.split('|')[0]

            #remove $ sign, convert to float
            price = price[1:]
            if price != "":
                price = float(price)

        if vendor == "nintendo":
            title = nintendoScraper.get_title(soup)
            price = nintendoScraper.get_price(soup)
            platform = nintendoScraper.get_platform(soup)

        if vendor == "steampowered":
            title, price, platform = steamAPI.getGame(url)
            #Steam stores price as integers, convert to float for comparison
            price = int(price) / 100.0

        if vendor == "xbox":
            title = xboxScraper.get_title(soup)
            price = xboxScraper.get_price(soup)
            platform = xboxScraper.get_platform(soup)

            #remove $ sign, convert to float
            price = price[1:]
            if price != "":
                price = float(price)

        if vendor == "playstation":
            title = psScraper.get_title(soup)
            price = psScraper.get_price(soup)
            platform = psScraper.get_platform(soup)

            #remove $ sign, convert to float
            price = price[1:]
            if price != "":
                price = float(price)

        gameID = ""
        gameDict = {'title': title, 'vendor': vendorHost, 'price': price, 'url': url, 'platform': platform, 'gameID': gameID}
        gameList.append(gameDict)

    return gameList

#Given game, add to json
def addGame(gameDict):
    with open(os.path.dirname(__file__) + '/../games.json', 'r+') as games:
        g = json.load(games)
        g.append(gameDict)
        games.seek(0)
        json.dump(g, games, indent=4)
