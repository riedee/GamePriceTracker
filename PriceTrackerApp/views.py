from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#def vue_test(request):
    #return render(request, 'PriceTrackerApp/vue-test.html')

def index(request):
    return HttpResponse("Welcome to Game Price Tracker!")
