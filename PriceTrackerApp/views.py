from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
import json

#models
from .models import *

with open('../games.json', 'r') as f:
    Games = json.load(f)

def isSubstring(value, substring):
    return substring.lower() in value.lower()

class HomeView(TemplateView):
	template_name = 'home.html'

def index(request):
    return HttpResponse("Welcome to Game Price Tracker!")
    
def search(request):
	#searchdata = Game.objects.filter()
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
    foundGames = [game for game in Games if isSubstring(game['gameTitle'], query)]
    for game in foundGames:
        game['slug'] = game['ID'] + '_' + game['console']
    context = { 'games' : foundGames }
    return render(request, 'search_results.html', context)


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
