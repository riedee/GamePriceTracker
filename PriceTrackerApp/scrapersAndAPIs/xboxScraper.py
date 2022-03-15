import bs4
from urllib.request import urlopen
from ..models import *

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
   

urlList = ["https://www.xbox.com/en-US/games/store/nhl-22-xbox-one/9NRDC9PXDQ5N/0010/9R9KBZNPNNHM"]

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
    vendor = Vendor(vendorName = vendorHost)
    vendor.save()
    #game = Game(gameTitle = title, bestVendor = vendor, lowestPrice = price, url = url, platform = platform, gameID = gameID)
    #game.save()

with open("allGameData.json", "w") as f:
    gameJson = json.dumps(gameList)
    f.write(gameJson)
    f.close