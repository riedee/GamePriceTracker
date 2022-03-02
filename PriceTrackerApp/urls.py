from django.urls import path
from .views import HomeView, SearchResultsView, GameView

urlpatterns = [
        path('search/', SearchResultsView.as_view(), name='search_results'),
        path('results/<int:id>', GameView.as_view(), name='game'),
        path('', HomeView.as_view(), name='home'),
]

