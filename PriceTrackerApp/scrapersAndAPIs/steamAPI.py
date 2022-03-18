import steamspypi
import json
#from ..models import *

def getGame(url):
    splitUrl = url.split('/')
    id = splitUrl[4]
    data_request = dict()
    data_request['request'] = 'appdetails'
    data_request['appid'] = id
    steamData = steamspypi.download(data_request)

    with open("dumped_data.json", "w") as jsonFile:
        json.dump(steamData, jsonFile, indent=4)

    f = open("dumped_data.json")
    game = json.load(f)
    gameTitle = game['name']
    gamePrice = game['price']

    return (gameTitle, gamePrice, "PC")
    
    '''gameID = id
    gameUrl = url
    vendor = Vendor(vendorName = 'Steam')
    vendor.save()
    gameDict = {'title': gameTitle, 'vendor': vendor, 'price': gamePrice, 'url': gameUrl, 'platform': "PC", 'gameID': gameID}
    with open("allGameData.json", "w") as games:
        gameJson = json.dumps(gameDict)
        games.write(gameJson)
        games.close()
    vendor = Vendor(vendorName = vendorHost)
    vendor.save()
    #game = Game(gameTitle = gameTitle, bestVendor = 'Steam', lowestPrice = gamePrice, url = gameUrl, platform = 'PC', gameID = gameID)
    #game.save()'''