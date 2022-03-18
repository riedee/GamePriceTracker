'''import bs4
import urllib
import json
from urllib.request import urlopen
from ..models import *'''


def get_title(soup): 
    try:
        # Outer Tag Object
        title_string = soup.find("h1", attrs={'class': 'Headingstyles__StyledH-sc-qpned7-0 HUGKw'}).string.strip()

    except AttributeError:
        title_string = ""   
 
    return title_string

def get_price(soup):
    try:
        price = soup.find("span", attrs={'class': 'ScreenReaderOnlystyles__StyledReaderText-sc-jiymtq-0 kXOKSo'}).string.strip()
#class="ScreenReaderOnlystyles__StyledReaderText-sc-jiymtq-0 kXOKSo" //inner
    except AttributeError:
        price = ""  
 
    return price
   
def get_platform(soup):
    try:
        platform = soup.find("div", attrs={'class': 'PlatformLabelstyles__StyledPlatform-sc-1cn94zq-0 gRaUjs'}).string.strip()
    except AttributeError:
        platform = ""
    
    return platform
   

'''urlList = ["https://www.nintendo.com/store/products/nba-2k22-switch/"]

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
    vendor = Vendor(vendorName = vendorHost)
    vendor.save()
    #game = Game(gameTitle = title, bestVendor = vendor, lowestPrice = price, url = url, platform = platform, gameID = gameID)
    #game.save()

with open("allGameData.json", "w") as f:
    gameJson = json.dumps(gameList)
    f.write(gameJson)
    f.close'''

