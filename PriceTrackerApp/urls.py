from django.urls import include, path
from .views import HomeView, SearchResultsView, GameView, VendorPageView, VendorView, RegisterView
from django.urls import re_path as url
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('search/', SearchResultsView, name='search_results'),
    path('register/', RegisterView, name='register'),
    path('results/<str:info>', GameView, name='game'),
    path('temporary', VendorView, name='vendor'),
        
    path('', HomeView, name='home'),
    path('#vendors', VendorPageView.as_view(), name='vendorpage'),
    path('accounts/', include('django.contrib.auth.urls')),
]

