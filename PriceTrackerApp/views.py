from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
import json
import os
from PriceTrackerApp import gamesearch

#models
from .models import *

with open(os.path.dirname(__file__) + '/../games.json', 'r') as f:
    Games = json.load(f)

def isSubstring(value, substring):
    return substring.lower() in value.lower()

class HomeView(TemplateView):
	template_name = 'home.html'
	
class VendorPageView(TemplateView):
	template_name = 'vendorpage.html'

def index(request):
    return HttpResponse("Welcome to Game Price Tracker!")
    
def search(request):
	#searchdata = Game.objects.filter()
    if request.POST:

        '''links = gamesearch.searchGame(request.POST['search'])
        gameList = gamesearch.scrapeGame(links)
        for game in gameList:
            gamesearch.addGame(game)'''
                             
        context = {

                        }
        return render(request, 'PriceTrackerApp/search_results.html', context)

def GameView(request, info):
    info = info.split('_')
    id = info[0]
    console = info[1]
    game = [game for game in Games if game['ID'] == id if game['console'] == console]
    if len(game):
        game = game[0]
        context = { 'game': game }
        return render(request, 'PriceTrackerApp/game.html', context)
    return HttpResponse("Game not found")

def SearchResultsView(request):
    query = request.GET['search']
    links = gamesearch.searchGame(query)
    gameList = gamesearch.scrapeGame(links)
    print(gameList)
    '''foundGames = [game for game in Games if isSubstring(game['gameTitle'], query)]
    for game in foundGames:
        game['slug'] = game['ID'] + '_' + game['console']'''
    context = { 'games' : gameList }
    return render(request, 'search_results.html', context)

def VendorView(request, id):
	vendorName = ''
	return 0
	

# class SearchResultsView(ListView):
#     model = Game
#     template_name = 'search_results.html'
#     context_object_name = 'object_list'

#     def get_queryset(self):
#        game = super(SearchResultsView, self).get_queryset()
#        query = self.request.GET.get('game')
#        if query:
#           postresult = Game.objects.filter(gameTitle__contains=query)
#           game = postresult
#        else:
#            game = None
#        return game
