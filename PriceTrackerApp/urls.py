from django.urls import path
from .views import HomeView, SearchResultsView, GameView

urlpatterns = [
        path('search/', SearchResultsView.as_view(), name='search_results'),
        path('results/<str:info>', GameView, name='game'),
        path('', HomeView.as_view(), name='home'),
]

