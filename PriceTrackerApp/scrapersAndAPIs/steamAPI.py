'''
The file scrapes information from Steam using an API
'''

import steamspypi
import json

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

    return (gameTitle, gamePrice, ["PC"])
