"""
A module to search for a specified game from approved vendors
Inputs: Search query, website links
"""


import urllib
import googlesearch
import requests
import bs4
from googlesearch import search
from bs4 import BeautifulSoup

#Import specific vendor scrapers
from PriceTrackerApp.scrapersAndAPIs import \
        amznScraper, nintendoScraper, steamAPI, xboxScraper, psScraper

def searchGame(query):
    """Returns list of links with their associated vendor name for a game specified"""

    #query should include 'buy', 'purchase', etc. at the end to bring up most useful results
    query = query + " buy"  
    links = []
    for i in search(query, tld="co.in", lang="en", country="na", user_agent=googlesearch.get_random_user_agent(), num=12, start=0, stop=10, pause=2):

        site = i.split(".")

        #list of vendors we know how to scrape info from
        vendors = ["steampowered", "xbox", "amazon", "nintendo", "playstation"]
        for j in vendors:
            if site[1] == j:
                soup = BeautifulSoup(requests.get(i).text, 'html.parser') 
                title = (soup.find_all('title')[0].get_text()).lower()

                #Often empty search results for sites will come up
                #as well as soundtracks and expansions for the game - remove them
                banned_keywords = ["search", "recommended", "soundtrack",
                        "expansion", "dlc", "bundle", "collector's"]

                if j != "amazon":
                    if all(i not in title for i in banned_keywords):
                        links.append((i, site[1]))
                #if the website is amazon, but sure result is from 'video games' category
                else:
                    headers = headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
                    'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                    'Accept-Language' : 'en-US,en;q=0.5',
                    'Accept-Encoding' : 'gzip',
                    'DNT' : '1', # Do Not Track Request Header
                    'Connection' : 'close'
                    }
                    page = requests.get(i, headers=headers)
                    soup  = bs4.BeautifulSoup(page.content, "html.parser")

                    try:
                        category = soup.find("a", attrs={'class' : 'a-link-normal a-color-tertiary'}).string.strip()
                    except AttributeError:
                        category = ""


                    if category == "Video Games":
                        if all(i not in title for i in banned_keywords):
                            links.append((i, site[1]))



    return links

def scrapeGame(links):
    """Given list of links with their associated website name, scrape info using appropriate scraper and return game dict"""
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
            if platform != "Platform Not Found":
                platform = platform.split(':')[1]
                platform = platform.split('|')[0]
                platform = platform.lstrip()
                platform = platform.rstrip()
                platform = [platform]

                #Amazon will sometimes include platform name in title - remove
                p = platform[0].lower()
                p = ''.join([i for i in p if not i.isdigit()])
                p = p.strip()
                p = p.capitalize()
                title = title.split(p)[0]
                title = title.rstrip()
                title = title.lstrip()

            #remove $ sign, convert to float
            price = price[1:]
            try:
                price = float(price)
            except ValueError:
                price = float('inf')

        if vendor == "nintendo":
            title = nintendoScraper.get_title(soup)
            price = nintendoScraper.get_price(soup)
            platform = [nintendoScraper.get_platform(soup)]

            #problem with scraping from nintendo
            try:
                price = float(price)
            except ValueError:
                price = float('inf')

        if vendor == "steampowered":
            title, price, platform = steamAPI.getGame(url)

            #Steam stores price as integers, convert to float for comparison
            if price:
                price = int(price) / 100.0
            else:
                price = 0.0

        if vendor == "xbox":
            title = xboxScraper.get_title(soup)
            price = xboxScraper.get_price(soup)
            platform = xboxScraper.get_platform(soup)

            title = title.rstrip()
            title = title.lstrip()

            #remove $ sign, convert to float
            price = price[1:]
            try:
                price = float(price)
            except ValueError:
                price = float('inf')

        if vendor == "playstation":
            title = psScraper.get_title(soup)
            price = psScraper.get_price(soup)
            platform = [psScraper.get_platform(soup)]

            #remove $ sign, convert to float
            price = price[1:]
            try:
                price = float(price)
            except ValueError:
                price = float('inf')

        if title is not None and title != "":
            #remove unicode
            title = title.encode("ascii", "ignore")
            title = title.decode()

            #get rid of console specific
            title = title.split(' PS')[0]
           
            if len(platform) > 0:
                gameID = title + platform[0]
                gameID = gameID.lower().replace(" ", "")
                gameID = ''.join(filter(str.isalnum, gameID))
            else:
                gameID = title
            gameDict = {'title': title, 'vendor': vendorHost, 'price': price, 'url': url, 'platform': platform, 'gameID': gameID}
            gameList.append(gameDict)

    return gameList
