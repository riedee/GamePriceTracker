"""
A module to update the prices for game(s) stored within the database with the current lowest price
Inputs: List of games
"""
import json
import os
from .models import *

'''
This method takes a list of game objects, and compares to currently saved games in the JSON
(if they exist), and replaces if the price is lower, and/or updates prices
'''
def saveGame(gameList):
    #Load saved games from games.json
    with open(os.path.dirname(__file__) + '/../games.json') as file:
        gameDict = json.load(file)
        
    for i in range(len(gameList)):
        #get the title, price, and url of the current game in gameList
        currTitle = gameList[i].get('title')
        currPrice = gameList[i].get('price')
        currUrl = gameList[i].get('url')

        #get all the currently saved games, do a case insensitive comparison
        #if the current game is not saved, save it
        games = gameDict.keys()
        if (all(j.casefold() != currTitle.casefold() for j in games)):
            gameDict[currTitle] = gameList[i]

        #else, make sure the currTitle is same as saved title (otherwise key error)
        else:
            for j in games:
                if j.casefold() == currTitle.casefold():
                    currTitle = j
            
            #If the saved url is the same as the current url, update (in case of price changes)
            if gameDict[currTitle].get('url') == currUrl:
               gameDict[currTitle] = gameList[i]     
            #else if the current game price is less than the price of the currently saved game, replace it
            elif type(currPrice) != str and currPrice < gameDict[currTitle].get('price'):
                gameDict[currTitle] = gameList[i]

    #save any/all changes  
    with open(os.path.dirname(__file__) + '/../games.json', 'w') as file:
        json.dump(gameDict, file, indent = 4)

    #Update each game in the JSON
    for key in gameDict:
        game = Game(gameTitle = key, bestVendor = gameDict[key].get('vendor'), lowestPrice = gameDict[key].get('price'), url = gameDict[key].get('url'), platform = gameDict[key].get('platform'), gameID = gameDict[key].get('gameID'))
        Game.objects.update_or_create(gameTitle=game.gameTitle)  

