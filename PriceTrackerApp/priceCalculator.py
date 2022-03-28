import json
import os
from .models import *

def saveGame(gameList):
    with open(os.path.dirname(__file__) + '/../games.json') as file:
        gameDict = json.load(file)
        
    for i in range(len(gameList)):
        currTitle = gameList[i].get('title')
        currVendor = gameList[i].get('vendor')
        currPrice = gameList[i].get('price')
        currUrl = gameList[i].get('url')
        currPlatform = gameList[i].get('platform')
        currGameID = gameList[i].get('gameID')
        if currTitle not in gameDict and currPrice != None:
            gameDict[currTitle] = gameList[i]
        else:
            if currPrice != None and currPrice < gameDict[currTitle].get('price'):
                gameDict[currTitle] = gameList[i]
        
    with open(os.path.dirname(__file__) + '/../games.json', 'w') as file:
        json.dump(gameDict, file, indent = 4)

    #for key in gameDict:
    #    game = Game(gameTitle = key, bestVendor = Vendor(gameDict[key].get('vendor')), lowestPrice = gameDict[key].get('price'), url = gameDict[key].get('url'), platform = gameDict[key].get('platform'), gameID = gameDict[key].get('gameID'))
    #    game.save()

