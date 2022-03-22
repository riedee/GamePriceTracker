from django.urls import path
from .views import HomeView, SearchResultsView, GameView, VendorPageView, VendorView, ProfileView, AmazonView
from django.conf.urls import include
from django.urls import re_path
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    path('search/', SearchResultsView, name='search_results'),
    path('results/<str:info>', GameView, name='game'),
 
    path('', HomeView.as_view(), name='home'),
    path('#vendors', VendorPageView.as_view(), name='vendorpage'),
    path('<int:user_id>/profile/', ProfileView, name='profile'),
    path('vendors/amazon/', AmazonView.as_view(), name = 'amazon'),
    #path('userlist', UserlistView, name='userlist'),

]

