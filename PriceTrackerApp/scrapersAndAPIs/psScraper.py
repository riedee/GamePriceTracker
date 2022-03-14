import bs4
from urllib.request import urlopen
from ..models import *

def get_title(soup): 
    try:
        # Outer Tag Object
        title = soup.select("h1.psw-m-b-5 psw-t-title-l psw-t-size-8 psw-l-line-break-word")[0].string.strip()
 
    except AttributeError:
        title_string = ""   
 
    return title_string

def get_price(soup):
    try:
        price = soup.find("span", attrs={'class':'psw-t-title-m', 'data-qa': 'mfeCtaMain#offer0#finalPrice'}).string.strip()
 
    except AttributeError:
        price = ""  
 
    return price
   

urlList = ["https://store.playstation.com/en-us/product/UP1003-CUSA00314_00-WOLFENSTEIN00001"]

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
    platform = "PS5"
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
