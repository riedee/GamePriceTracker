import urllib
import requests
import bs4
import json
from googlesearch import search
from bs4 import BeautifulSoup
from urllib.request import urlopen

#from scrapersAndAPIs import amznScraper, nintendoScraper, psScraper, steamAPI, xboxScraper
import scrapersAndAPIs.amznScraper as amznScraper
import scrapersAndAPIs.nintendoScraper as nintendoScraper
import scrapersAndAPIs.steamAPI as steamAPI
import scrapersAndAPIs.xboxScraper as xboxScraper
import scrapersAndAPIs.psScraper as psScraper

#Returns list of links with their associated vendor name for a game specified
def searchGame(query):
    #query should include 'buy', 'purchase', etc. at the end to bring up most useful results
    query = query + " buy"
    links = []
    for i in search(query, tld="co.in", num=15, stop=15, pause=3):
        site = i.split(".")
        store = i.split("/")

        #list of vendors we know how to scrape info from
        vendors = ["steampowered", "xbox", "amazon", "nintendo", "playstation"]
        #store_links = ["app", "games", "products", "dp", "products"] #store[2], store[3]
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

#Given list of links with their associated website name, scrape info using appropriate scraper and return game objects
def scrapeGame(links):
    gameList = []
    for url, vendor in links:
        #page = urlopen(url)
        #html = page.read().decode("utf-8")
        #soup = bs4.BeautifulSoup(html, "html.parser")
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
            #price is stored as ints
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
    with open("allGameData.json", "w") as games:
        gameJson = json.dumps(gameDict)
        games.write(gameJson)
        games.close()