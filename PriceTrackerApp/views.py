from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ObjectDoesNotExist
from PriceTrackerApp.forms import RegistrationForm
from django.contrib.auth.decorators import user_passes_test
import json
import os
from PriceTrackerApp import gamesearch
from PriceTrackerApp import priceCalculator

#models
from .models import *

with open(os.path.dirname(__file__) + '/../games.json', 'r') as f:
    Games = json.load(f)

def isSubstring(value, substring):
    return substring.lower() in value.lower()

def HomeView(request):
    print(request.user.username)
    username = request.user.username if request.user.is_authenticated else ''
    return render(request, 'home.html', {'username' : username})
	
class VendorPageView(TemplateView):
	template_name = 'vendorpage.html'

class AmazonView(TemplateView):
	template_name = 'amazon.html'

class PlayStationView(TemplateView):
	template_name = 'psvendor.html'

class NintendoView(TemplateView):
	template_name = 'nintendo.html'

class MicrosoftView(TemplateView):
	template_name = 'microsoft.html'

class SteamView(TemplateView):
	template_name = 'steam.html'

class LoginView(TemplateView):
    template_name = 'login.html'

class DirectoryView(TemplateView):
    template_name = 'userdirectory.html'

class GameHomeView(TemplateView):
    template_name = 'gamepage.html'

def index(request):
    return HttpResponse("Welcome to Game Price Tracker!")

def favGame(request):
    game = request.POST['info']
    user_id = request.POST['user_id']
    
    try:
        uid = User.objects.get(pk=user_id)
        profile = uid.profile
        profile.saved_game = game
        profile.save()
    except ObjectDoesNotExist:
        print("test")
        return HttpResponse("The user_id given does not match any user_id in the system")

    return HttpResponse("Added game to saved games")

'''def search(request):                  
    context = {

                    }
    return render(request, 'PriceTrackerApp/search_results.html', context)'''

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

    #begin by searching for game in JSON
    #if found, display that to user
    #give option to show more results
    #otherwise search internet and show results

    #query internet for relevant vendor webpages
    links = gamesearch.searchGame(query)
    #scrape webpages and create game objects
    gameList = gamesearch.scrapeGame(links)


    if len(gameList) > 0:
        #update JSON file of saved games
        priceCalculator.saveGame(gameList)

        #search JSON for game (take first result from gameList since that's likely to be more accurate result)
        with open(os.path.dirname(__file__) + '/../games.json') as file:
            gameDict = json.load(file)
        
        title = None
        for j in gameDict.keys():
            if j.casefold() == gameList[0].get('title').casefold():
                title = j

        gameList_sorted = sorted(gameList, key = lambda i:i['price'])

        context = { 'games' : gameList_sorted, 'bestGame' : gameDict[title]}

    #game list is empty - no results found
    else:
        context = {}

    return render(request, 'search_results.html', context)

def FavGameView(request):
    context = {}
    return render(request, 'search_results.html', context)

def VendorView(request):
	return 0

#display personal info of user
def ProfileView(request, user_id):
    #Try to get user ID
    try:
        uid = User.objects.get(pk=user_id)
    except ObjectDoesNotExist:
        return HttpResponse("The user_id given does not match any user_id in the system")
    if (uid.profile.saved_game == ''):
        game = ''
    else:
        game = [uid.profile.saved_game]
    data = Profile(user_id=uid, username = uid.username, email = uid.email, fn = uid.first_name, ln = uid.last_name, saved_game=game)
    if uid.id != request.user.id:
        return HttpResponse("You are not authenticated as desired user profile")
    context = {'user_id': uid,
            'data': data,
            'assigned': uid,
            }
    return render(request, "PriceTrackerApp/profile.html", context)

def RegisterView(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

def UserDirectoryView(request):
	data = User.objects.all()
	context = {'data': data,
	}
	return render(request, "PriceTrackerApp/userdirectory.html", context)
