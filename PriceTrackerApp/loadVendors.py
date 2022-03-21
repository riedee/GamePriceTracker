from .models import *
import json

amazon = Vendor(vendorName = "Amazon", storeFront = "https://www.amazon.com")
amazon.save()
amznDict = {'vendorName': 'Amazon', 'storeFront': "https://www.amazon.com"}
ps = Vendor(vendorName = "Playstation Store", storeFront = "https://store.playstation.com/en-us")
ps.save()
psDict = {'vendorName': 'Playstation Store', 'storeFront': "https://store.playstation.com/en-us"}
nintendo = Vendor(vendorName = "Nintendo eShop", storeFront = "https://store.playstation.com/en-us")
nintendo.save()
nintendoDict = {'vendorName': 'Nintendo eShop', 'storeFront': "https://www.nintendo.com/store"}
xbox = Vendor(vendorName = "Microsoft Store", storeFront = "https://www.xbox.com/en-US/microsoft-store")
xbox.save()
xboxDict = {'vendorName': 'Microsoft Store', 'storeFront': "https://www.xbox.com/en-US/microsoft-store"}
steam = Vendor(vendorName = "Steam", storeFront = "https://store.steampowered.com")
steam.save()
steamDict = {'vendorName': 'Steam', 'storeFront': "https://store.steampowered.com"}

with open('vendors.json', 'w') as jsonFile:
    json.dump(amznDict, jsonFile)
    json.dump(psDict, jsonFile)
    json.dump(nintendoDict, jsonFile)
    json.dump(xboxDict, jsonFile)
    json.dump(steamDict, jsonFile)