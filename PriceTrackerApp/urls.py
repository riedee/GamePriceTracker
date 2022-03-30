from django.urls import include, path
from .views import HomeView, SearchResultsView, GameView, VendorPageView, VendorView, ProfileView, RegisterView, AmazonView, PlayStationView, NintendoView, MicrosoftView, SteamView, LoginView
from django.conf.urls import include
from django.urls import re_path
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    path('search/', SearchResultsView, name='search_results'),
    path('register/', RegisterView, name='register'),
    path('results/<str:info>', GameView, name='game'),
    path('login', LoginView.as_view(), name='login'),
    path('home', HomeView, name='home'),
    path('vendors', VendorPageView.as_view(), name='vendorpage'),
    path('<int:user_id>/profile/', ProfileView, name='profile'),
    path('vendors/amazon/', AmazonView.as_view(), name = 'amazon'),
    path('vendors/playstation/', PlayStationView.as_view(), name = 'ps'),
    path('vendors/nintendo/', NintendoView.as_view(), name = 'nintendo'),
    path('vendors/microsoft/', MicrosoftView.as_view(), name = 'microsoft'),
    path('vendors/steam/', SteamView.as_view(), name = 'steam'),
    path('accounts/', include('django.contrib.auth.urls')),
    
    #path('userlist', UserlistView, name='userlist'),

]

