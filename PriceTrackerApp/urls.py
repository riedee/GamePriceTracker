from django.urls import path
from django.contrib import admin
from .views import HomeView, SearchResultsView
from . import views

urlpatterns = [
		path('admin/', admin.site.urls),
        path('search/', SearchResultsView.as_view(), name='search_results'),
        path('', HomeView.as_view(), name='home'),
        path('profile/', views.profile, name='profile'),
        
]

