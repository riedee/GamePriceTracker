from django.urls import path
from .views import HomeView, SearchResultsView

urlpatterns = [
        path('search/', SearchResultsView.as_view(), name='search_results'),
        path('', HomeView.as_view(), name='home'),
]

