from django.urls import path
from .views import HomeView, SearchResultsView, GameView, VendorView

urlpatterns = [
        path('search/', SearchResultsView, name='search_results'),
        path('results/<str:info>', GameView, name='game'),
        path('<str:vendorName>', VendorView, name='vendor'),
        path('', HomeView.as_view(), name='home'),
]

