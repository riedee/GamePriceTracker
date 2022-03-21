from django.urls import path
from .views import HomeView, SearchResultsView, GameView, VendorPageView, VendorView
from django.urls import include, re_path
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    path('search/', SearchResultsView, name='search_results'),
    path('results/<str:info>', GameView, name='game'),
    path('temporary', VendorView, name='vendor'),
        
    path('', HomeView.as_view(), name='home'),
    path('#vendors', VendorPageView.as_view(), name='vendorpage'),
]

