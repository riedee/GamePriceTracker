"""
A module relating links to view objects
Inputs: view objects
"""

from django.urls import include, path
from django.urls import re_path
from django.contrib import admin
from .views import *

admin.autodiscover()

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    path('search/', SearchResultsView, name='search_results'),
    path('register/', RegisterView, name='register'),
    path('results/<str:info>', GameView, name='game'),
    path('games', GameViewAll, name='gamehome'),
    path('login', LoginView.as_view(), name='login'),
    path('home', HomeView, name='home'),
    path('vendors', VendorPageView.as_view(), name='vendorpage'),
    path('favorite', favGame, name="python_file"),
    path('search/filter', FilterView, name="filter"),
    path('remove', removeGame, name ='removeGame'),
    path('profile', DirectoryView.as_view(), name='directory'),
    path('<int:user_id>/profile/', ProfileView, name='profile'),
    path('vendors/amazon/', AmazonView.as_view(), name = 'amazon'),
    path('vendors/playstation/', PlayStationView.as_view(), name = 'ps'),
    path('vendors/nintendo/', NintendoView.as_view(), name = 'nintendo'),
    path('vendors/microsoft/', MicrosoftView.as_view(), name = 'microsoft'),
    path('vendors/steam/', SteamView.as_view(), name = 'steam'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('directory/', UserDirectoryView, name='userdirectory'),
]
