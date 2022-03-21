from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
import json

#models
from .models import *

with open('./games.json', 'r') as f:
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

def VendorView(request):
	vendorName = ''
	return 0

#display personal info of user
def ProfileView(request, user_id):
    #Try to get user ID
    try:
        uid = User.objects.get(pk=user_id)
    except ObjectDoesNotExist:
        return HttpResponse("The user_id given does not match any user_id in the system")
    data = Profile(user_id=uid, username = uid.username, email = uid.email, fn = uid.first_name, ln = uid.last_name)
    context = {'user_id': uid,
            'data': data,
            'assigned': uid,
            }
    return render(request, "PriceTrackerApp/profile.html", context)
