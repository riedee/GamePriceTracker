'''
This file scrapes information from the Xbos store by looking at specific elements
'''

def get_title(soup): 
    try:
        # Outer Tag Object
        title_string = soup.find("h1", attrs={'class':'typography-module__xdsH1___zrXla ProductDetailsHeader-module__productTitle___l-kbD'}).string.strip()
 
    except AttributeError:
        title_string = ""   
 
    title_string = title_string.split("for")[0]
    title_string = title_string.split("(")[0]

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
        plat = soup.find("div", attrs={'class':'FeaturesList-module__wrapper___uUx0S'}).find_all("div")
        platform = []
        for p in plat:
            platform.append(p.text)
   
    except AttributeError:
        platform = ""

    return platform
