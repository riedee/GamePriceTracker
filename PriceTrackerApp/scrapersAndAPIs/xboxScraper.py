'''import bs4
import urllib
import json
from urllib.request import urlopen
from ..models import *'''

def get_title(soup): 
    try:
        # Outer Tag Object
        title_string = soup.find("h1", attrs={'class':'typography-module__xdsH1___zrXla ProductDetailsHeader-module__productTitle___l-kbD'}).string.strip()
 
    except AttributeError:
        title_string = ""   
 
    return title_string

def get_price(soup):
    try:
        price = soup.find("span", attrs={'class':'Price-module__srOnly___2mBg_'}).string.strip()
        if ' ' in price:
            priceList = price.split(' ')
            price = priceList[len(priceList)-1] 
    except AttributeError:
        price = ""  
 
    return price

def get_platform(soup):
    try:
        plat = soup.find("div", attrs={'class':'FeaturesList-module__wrapper___uUx0S'}).find_all("div", attrs={'class':'FeaturesList-module__item___19NYe typography-module__xdsTag3___dtX8u'})
        platform = []
        for p in plat:
            platform.append(p.text)
   
    except AttributeError:
        platform = ""

    return platform

'''urlList = ["https://www.xbox.com/en-US/games/store/nhl-22-xbox-one/9NRDC9PXDQ5N/0010/9R9KBZNPNNHM"]

gameList = []

for i in range(len(urlList)):
    url = urlList[i]
    page = urlopen(url)
    html = page.read().decode("utf-8")
    soup = bs4.BeautifulSoup(html, "html.parser")
    parsed_url = urllib.parse.urlparse(url)
    vendorHost = parsed_url.netloc.string.strip()
    title = get_title(soup)
    price = get_price(soup)
    platform = "Xbox One"
    gameID = title + platform
    gameDict = {'title': title, 'vendor': vendorHost, 'price': price, 'url': url, 'platform': platform, 'gameID': gameID}
    gameList.append(gameDict)
    vendor = Vendor(vendorName = vendorHost, storeFront = "https://www.xbox.com/en-US")
    vendor.save()
    #game = Game(gameTitle = title, bestVendor = vendor, lowestPrice = price, url = url, platform = platform, gameID = gameID)
    #game.save()

with open("allGameData.json", "w") as f:
    gameJson = json.dumps(gameList)
    f.write(gameJson)
    f.close'''