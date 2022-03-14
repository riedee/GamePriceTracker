import json
from platform import platform
from .models import *

file = open("allGameData.json", "r")
content = file.read()
gameList = json.loads(content)
gameDict = {}
for i in range(len(gameList)):
    currTitle = gameList[i]['title']
    currVendor = gameList[i]['vendor']
    currPrice = gameList[i]['price']
    currUrl = gameList[i]['url']
    currPlatform = gameList[i]['platform']
    currGameID = gameList[i]['gameID']
    if currTitle not in gameDict:
        gameDict[currTitle] = (currVendor, currPrice, currUrl, currPlatform, currGameID)
    else:
        if currPrice < gameDict[currTitle][1]:
            gameDict[currTitle][0] = currVendor
            gameDict[currTitle][1] = currPrice
            gameDict[currTitle][2] = currUrl

for key in gameDict:
    game = Game(gameTitle = key, bestVendor = gameDict[key][0], lowestPrice = gameDict[key][1], url = gameDict[key][2], platform = gameDict[key][3], gameID = gameDict[key][4])
    game.save()

