from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView

#models
from .models import *

class HomeView(TemplateView):
	template_name = 'home.html'

def index(request):
    return HttpResponse("Welcome to Game Price Tracker!")
    
def search(request):
	#searchdata = Game.objects.filter()
	context = {
                        }
	return render(request, 'PriceTrackerApp/search_results.html', context)

def GameView(request, id):
    game = Game.objects.filter(id=id)[0]
    context = { 'game': game }
    return render(request, 'PriceTrackerApp/game.html', context)

class SearchResultsView(ListView):
    model = Game
    template_name = 'search_results.html'
    context_object_name = 'object_list'

    def get_queryset(self):
       game = super(SearchResultsView, self).get_queryset()
       query = self.request.GET.get('game')
       if query:
          postresult = Game.objects.filter(gameTitle__contains=query)
          game = postresult
       else:
           game = None
       return game

