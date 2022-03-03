from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User

import json

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

#display personal info of user
def profile(request):
    #Try to get user ID
	try:
		current_user = User.objects.get(pk=request.user.id)
	except ObjectDoesNotExist:
		return HttpResponse("The user given does not match any user in the system")
	data = Profile(user_id=current_user.id, username = current_user.username, email = current_user.email, fn = current_user.first_name, ln = current_user.last_name)
	context = {'user_id': user_id,
            'data': data,}
	return render(request, "PriceTrackerApp/personal.html", context)
