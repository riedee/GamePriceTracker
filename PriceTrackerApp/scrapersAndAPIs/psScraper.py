'''
The file scrapes for the PS store by looking at specific elements
'''

def get_title(soup): 
    """Scrape game title"""
    try:
        # Outer Tag Object
        title_string = soup.find("h1", attrs={'class': 'psw-m-b-5 psw-t-title-l psw-t-size-8 psw-l-line-break-word'}).string.strip()

    except AttributeError:
        title_string = ""

    return title_string

def get_price(soup):
    """Scrape game price"""
    try:
        price = soup.find("span", attrs={'class':'psw-t-title-m', 'data-qa': 'mfeCtaMain#offer0#finalPrice'}).string.strip()

    except AttributeError:
        price = ""

    return price

def get_platform(soup):
    """Scrape platforms"""
    try:
        platform = soup.find("dd", attrs={'class':'psw-p-r-6 psw-p-r-0@tablet-s psw-t-bold psw-l-w-1/2 psw-l-w-1/6@tablet-s psw-l-w-1/6@tablet-l psw-l-w-1/8@laptop psw-l-w-1/6@desktop psw-l-w-1/6@max'}).string.strip()

    except AttributeError:
        platform = ""

    return platform
