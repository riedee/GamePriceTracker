"""
A module handling page logic and routing

Views:
HomeView
VendorPageView
AmazonView
PlayStationView
NintendoView
MicrosoftView
SteamView
LoginView
DirectroyView
GameHomeView
index
FavGameView
removeGame
favGame
GameView
SearchResultsView
GameViewAll
ProfleView
RegisterView
UserDirectoryView
"""

import json
import os
import ast
import operator

from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.contrib.auth import login, authenticate
from django.core.exceptions import ObjectDoesNotExist
from PriceTrackerApp.forms import RegistrationForm
from PriceTrackerApp import gamesearch
from PriceTrackerApp import priceCalculator

#models
from .models import Game, User, Profile

class VendorPageView(TemplateView):
    """Displays the list of vendors"""
    template_name = 'vendorpage.html'

class AmazonView(TemplateView):
    """Displays the Amazon vendor page"""
    template_name = 'amazon.html'

class PlayStationView(TemplateView):
    """Displays the PS vendor page"""
    template_name = 'psvendor.html'

class NintendoView(TemplateView):
    """Displays the Nintendo vendor page"""
    template_name = 'nintendo.html'

class MicrosoftView(TemplateView):
    """Displays the MS vendor page"""
    template_name = 'microsoft.html'

class SteamView(TemplateView):
    """Displays the Steam vendor page"""
    template_name = 'steam.html'

class LoginView(TemplateView):
    """Displays the login page"""
    template_name = 'login.html'

class DirectoryView(TemplateView):
    """Displays the user directory"""
    template_name = 'userdirectory.html'

class GameHomeView(TemplateView):
    """Displays the list of games"""
    template_name = 'gamepage.html'

def HomeView(request):
    """Displays the homepage"""
    print(request.user.username)
    username = request.user.username if request.user.is_authenticated else ''
    return render(request, 'home.html', {'username' : username})

def FavGameView(request):
    """Favorite game without reloading search result page"""
    context = {}
    return render(request, 'search_results.html', context)

def removeGame(request):
    """Remove game from favorites"""
    #game_title = request.POST['info']
    user_id = request.POST['user_id']
    
    try:
        uid = User.objects.get(pk=user_id)
        profile = uid.profile
        profile.saved_game = None
        profile.save()
    except ObjectDoesNotExist:
        return HttpResponse("The user_id given does not match any user_id in the system")

    return render(request, 'profile.html', {})

def favGame(request):
    """Process a user favoriting a game"""
    game_title = request.POST['info']
    user_id = request.POST['user_id']

    with open(os.path.dirname(__file__) + '/../games.json') as file:
        gameDict = json.load(file)

    game = gameDict[game_title]
   
    try:
        uid = User.objects.get(pk=user_id)
        profile = uid.profile
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
    """Display all games"""
    try:
        game = get_object_or_404(Game, gameTitle=info)
        context = {'game': game}
    
        return render(request,'PriceTrackerApp/game.html', context)
    except LookupError:
        return HttpResponse("Game not found")

def FilterView(request):
    """Process game filtering"""
    games = request.POST.get('games_restrict', False)
    games_all = request.POST.get('games_all', False)
    consoles = request.POST.get('consoles', False)
    filter_game = request.POST.get('filter', False)
    checked = request.POST.get('checked', False)

    #games = json.dumps(games)
    #games_all = json.dumps(games_all)
    games = ast.literal_eval(games)
    games_all = ast.literal_eval(games_all)
    consoles = consoles.strip('][').replace("'", "").split(', ')

    if checked == 'false':
        checked = 0
    else:
        checked = 1
    
    if not checked:
        consoles.remove(filter_game)
    else:
        if filter_game not in consoles:
            consoles.append(filter_game)

    new_game_list = []
    for g in games_all:
        for c in g['platform']:
            if c in consoles:
                new_game_list.append(g)
                break

    context = {'games_all': games_all, 'bestGame': '', 'games_restrict': new_game_list, 'consoles': consoles}
    return render(request, 'search_results.html', context)


def SearchResultsView(request):
    """Process a search query"""
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

        context = { 'games_all' : gameList_sorted, 'bestGame' : gameDict[title], 'games_restrict': gameList_sorted, 'consoles': ["PC", "Xbox", "Nintendo", "PS"]}

    #game list is empty - no results found
    else:
        context = {}

    return render(request, 'search_results.html', context)

def GameViewAll(request):
    """View all games"""
    data = Game.objects.all()
    data = sorted(data, key=operator.attrgetter('gameTitle'))
    context = {'games': data}
    return render(request, 'gamepage.html', context)

def ProfileView(request, user_id):
    """Display personal info of user"""
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
    """Display registration form"""
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
    """Displays all users"""
    data = User.objects.all()
    context = {'data': data,
	}
    return render(request, "PriceTrackerApp/userdirectory.html", context)
