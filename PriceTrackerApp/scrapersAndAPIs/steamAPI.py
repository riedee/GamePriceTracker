'''
The file scrapes information from Steam using an API
'''

import json
import steamspypi

def getGame(url):
    """Scrap game info"""
    splitUrl = url.split('/')
    game_id = splitUrl[4]
    data_request = dict()
    data_request['request'] = 'appdetails'
    data_request['appid'] = game_id
    steamData = steamspypi.download(data_request)

    with open("dumped_data.json", "w", encoding='utf-8') as jsonFile:
        json.dump(steamData, jsonFile, indent=4)

    f = open("dumped_data.json", encoding='utf-8')
    game = json.load(f)
    gameTitle = game['name']
    gamePrice = game['price']

    return (gameTitle, gamePrice, ["PC"])
