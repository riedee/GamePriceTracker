import bs4
from urllib.request import urlopen
from .models import *

url = "https://www.amazon.com/Pokemon-Legends-Arceus-Nintendo-Switch/dp/B09BNK4592/ref=sr_1_1_sspa?keywords=pokemon%2Blegends%2Barceus%2Bnintendo%2Bswitch&qid=1646319774&sprefix=pokemon%2B%2Caps%2C66&sr=8-1-spons&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFYUUo0WDJMWUpZUlcmZW5jcnlwdGVkSWQ9QTAwMDU0NDIzTkVSUDhVSENUQ0dFJmVuY3J5cHRlZEFkSWQ9QTA4Njk2NTczVThSMEpLR1E1REJWJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ&th=1"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = bs4.BeautifulSoup(html, "html.parser")

parsed_url = urllib.parse.urlparse(url)
vendorHost = parsed_url.netloc.string.strip()

def get_title(soup): 
    try:
        # Outer Tag Object
        title = soup.find("span", attrs={"id":'productTitle'})
 
        # Inner NavigableString Object
        title_value = title.string
 
        # Title as a string value
        title_string = title_value.strip()
 
    except AttributeError:
        title_string = ""   
 
    return title_string

def get_price(soup):
    try:
        price = soup.find("span", attrs={'id':'priceblock_ourprice'}).string.strip()
 
    except AttributeError:
        price = ""  
 
    return price

def get_platform(soup):
    try:
        platform = soup.find("div", attrs={'id':'variation_platform_display'})
        platform = platform.find("span").string.strip()
 
    except AttributeError:
        platform = "Platform Not Found"
 
    return platform   

title = get_title(soup)
price = get_price(soup)
platform = get_platform(soup)
gameID = title + platform
vendor = Vendor(vendorName = vendorHost)
vendor.save()
game = Game(gameTitle = title, bestVendor = vendor, lowestPrice = price, url = url, platform = platform, gameID = gameID)
game.save()