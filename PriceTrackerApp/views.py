from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView


#models
from .models import *

def index(request):
    return HttpResponse("Welcome to Game Price Tracker!")
    
def search(request):
	#searchdata = Game.objects.filter()
	context = {
                        }
	return render(request, 'PriceTrackerApp/search.html', context)

class SearchView(ListView):
    model = Game
    template_name = 'search_results.html'
    context_object_name = 'all_search_results'

    def get_queryset(self):
       result = super(SearchView, self).get_queryset()
       query = self.request.GET.get('search')
       if query:
          postresult = Game.objects.filter(gameTitle__contains=query)
          result = postresult
       else:
           result = None
       return result
