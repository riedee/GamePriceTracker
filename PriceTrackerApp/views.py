from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from PriceTrackerApp.forms import RegistrationForm
from django.contrib.auth.decorators import user_passes_test
import json
import os
from PriceTrackerApp import gamesearch
from PriceTrackerApp import priceCalculator

#models
from .models import *

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

#Favorite game without reloading search result page
def FavGameView(request):
    context = {}
    return render(request, 'search_results.html', context)

def removeGame(request):
    game_title = request.POST['info']
    user_id = request.POST['user_id']
    
    try:
        uid = User.objects.get(pk=user_id)
        profile = uid.profile
        profile.saved_game = None
        profile.save()
    except ObjectDoesNotExist:
        return HttpResponse("The user_id given does not match any user_id in the system")

    #return HttpResponse("Game removed from saved games")
    return render(request, 'profile.html', {})

#Process a user favoriting a game
def favGame(request):
    game_title = request.POST['info']
    user_id = request.POST['user_id']

    with open(os.path.dirname(__file__) + '/../games.json') as file:
            gameDict = json.load(file)

    game = gameDict[game_title]
    
    try:
        uid = User.objects.get(pk=user_id)
        profile = uid.profile
        #game_test = Game(gameTitle=game_title, bestVendor=game.get('vendor'), lowestPrice=game.get('price'), url=game.get('url'), platform=game.get('platform')[0], gameID=game.get('gameID'))
        game_test = Game(gameTitle=game_title, bestVendor=game.get('vendor'), lowestPrice=game.get('price'), url=game.get('url'), platform=game.get('platform')[0], gameID=game.get('gameID'))
        obj = Game.objects.get(gameTitle = game_test.gameTitle)
        if (profile.saved_game != obj):
            profile.saved_game = obj
            obj.save()
            profile.save()
            return HttpResponse("Added game to saved games")
        else:
            profile.saved_game = None
            obj.save()
            profile.save()
            return HttpResponse("Game removed from saved games")

    except ObjectDoesNotExist:
        return HttpResponse("The user_id given does not match any user_id in the system")

def GameView(request, info):   
    with open(os.path.dirname(__file__) + '/../games.json') as file:
            gameDict = json.load(file)

    try:
        game = get_object_or_404(Game, gameTitle=info)
        context = {'game': game}
    
        return render(request,'PriceTrackerApp/game.html', context)
    except:
        return HttpResponse("Game not found")

#Process a search query
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

def GameViewAll(request):
    data = Game.objects.all()
    context = {'games': data}
    return render(request, 'gamepage.html', context)

def VendorView(request):
	return 0

#display personal info of user
def ProfileView(request, user_id):
    #Try to get user ID
    try:
        uid = User.objects.get(pk=user_id)
    except ObjectDoesNotExist:
        return HttpResponse("The user_id given does not match any user_id in the system")
    if (uid.profile.saved_game == None):
        game = None
    else:
        game = uid.profile.saved_game
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
