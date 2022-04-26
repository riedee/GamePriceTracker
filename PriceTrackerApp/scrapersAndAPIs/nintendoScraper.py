'''
This file scrapes information from Nintendo by looking at specific elements
'''

def get_title(soup): 
    """Scrape game title"""
    try:
        # Outer Tag Object
        title_string = soup.find("h1", attrs={'class': 'Headingstyles__StyledH-sc-qpned7-0 HUGKw'}).string.strip()

    except AttributeError:
        title_string = ""

    return title_string

def get_price(soup):
    """Scrape game price"""
    try:
        price = soup.find("div", attrs={'class':'Pricestyles__PriceWrapper-sc-afjfk5-8 eimTmx'}).string.strip()

    except AttributeError:
        price = ""

    return price


def get_platform(soup):
    """Scrape platforms"""
    try:
        platform = soup.find("div", attrs={'class': 'PlatformLabelstyles__StyledPlatform-sc-1cn94zq-0 gRaUjs'}).string.strip()
    except AttributeError:
        platform = ""

    return platform
