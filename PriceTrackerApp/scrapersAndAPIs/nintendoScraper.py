import bs4
from urllib.request import urlopen
from ..models import *

def get_title(soup): 
    try:
        # Outer Tag Object
        title_string = soup.select("h1.Headingstyles__StyledH-sc-qpned7-0 HUGKw")[0].string.strip()
    except AttributeError:
        title_string = ""   
 
    return title_string

def get_price(soup):
    try:
        price = soup.find("span", attrs={'class':'ScreenReaderOnlystyles__StyledReaderText-sc-jiymtq-0 kXOKSo'}).string.strip()

    except AttributeError:
        price = ""  
 
    return price
   

urlList = ["https://www.nintendo.com/store/products/nba-2k22-switch/"]

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
    platform = 'Nintendo Switch'
    gameID = title + platform
    gameDict = {'title': title, 'vendor': vendorHost, 'price': price, 'url': url, 'platform': platform, 'gameID': gameID}
    gameList.append(gameDict)
    vendor = Vendor(vendorName = vendorHost, storeFront = "https://www.nintendo.com/store")
    vendor.save()
    #game = Game(gameTitle = title, bestVendor = vendor, lowestPrice = price, url = url, platform = platform, gameID = gameID)
    #game.save()

with open("allGameData.json", "w") as f:
    gameJson = json.dumps(gameList)
    f.write(gameJson)
    f.close

