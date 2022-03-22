from django.urls import path
from .views import HomeView, SearchResultsView, GameView, VendorPageView, VendorView, ProfileView, AmazonView, PlayStationView, NintendoView, MicrosoftView, SteamView
from django.conf.urls import include, url
from django.urls import re_path as url
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('search/', SearchResultsView, name='search_results'),
    path('results/<str:info>', GameView, name='game'),
 
    path('', HomeView.as_view(), name='home'),
    path('#vendors', VendorPageView.as_view(), name='vendorpage'),
    path('<int:user_id>/profile/', ProfileView, name='profile'),
    path('vendors/amazon/', AmazonView.as_view(), name = 'amazon'),
    path('vendors/playstation/', PlayStationView.as_view(), name = 'ps'),
    path('vendors/nintendo/', NintendoView.as_view(), name = 'nintendo'),
    path('vendors/microsoft/', MicrosoftView.as_view(), name = 'microsoft'),
    path('vendors/steam/', SteamView.as_view(), name = 'steam'),
    
    #path('userlist', UserlistView, name='userlist'),

]

