from django.urls import path
from .views import HomeView, SearchResultsView, GameView, VendorPageView, VendorView, ProfileView
from django.conf.urls import include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('search/', SearchResultsView, name='search_results'),
    path('results/<str:info>', GameView, name='game'),
    path('temporary', VendorView, name='vendor'),
        
    path('', HomeView.as_view(), name='home'),
    path('#vendors', VendorPageView.as_view(), name='vendorpage'),
    path('<int:user_id>/profile/', ProfileView, name='profile'),
    #path('userlist', Userlist, name='userlist'),

]

