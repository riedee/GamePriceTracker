from googlesearch import search
import requests
from bs4 import BeautifulSoup

#query should include 'buy' at the end to bring up most useful results
def searchGame(query):
    links = []
    for i in search(query, tld="co.in", num=15, stop=15, pause=3):
        site = i.split(".")

        #list of vendors, replace when we have list of specific vendors we're looking at
        vendors = ["steampowered", "microsoft", "nintendo", "amazon", "playstation"]
        for j in vendors:
            if site[1] == j:
                soup = BeautifulSoup(requests.get(i).text, 'html.parser')
                
                links.append(soup.find_all('title')[0].get_text())
                links.append(i)

    return links