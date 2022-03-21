from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
import json

from PriceTrackerApp.forms import RegistrationForm

#models
from .models import *

with open('./games.json', 'r') as f:
    Games = json.load(f)

def isSubstring(value, substring):
    return substring.lower() in value.lower()


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

def HomeView(request):
    print(request.user.username)
    username = request.user.username if request.user.is_authenticated else ''
    return render(request, 'PriceTrackerApp/home.html', {'username' : username})
	
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
