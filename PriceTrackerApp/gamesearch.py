from googlesearch import search
import requests
from bs4 import BeautifulSoup

#query should include 'buy', 'purchase', etc. at the end to bring up most useful results
def searchGame(query):
    links = []
    for i in search(query, tld="co.in", num=15, stop=15, pause=3):
        site = i.split(".")

        #list of vendors we know how to scrape info from
        vendors = ["steampowered", "microsoft", "nintendo", "amazon", "playstation"]
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