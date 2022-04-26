'''
This file scrapes information from Amazon by looking at specific elements
'''

def get_title(soup):
    """Scrape game title"""
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
    """Scrape game price"""
    #If unable to find price in regular section, try "new and used"
    try:
        price = soup.find("span", attrs={'id':'priceblock_ourprice'}).string.strip()
    except AttributeError:
        try:
            price = soup.find("span", attrs={'class':'a-size-base a-color-price'}).string.strip()
        except AttributeError:
            price = ""

    return price

def get_platform(soup):
    """Scrape platform types"""
    try:
        platform = soup.find("div", attrs={'id':'platformInformation_feature_div'}).text

    except AttributeError:
        platform = "Platform Not Found"

    return platform
