from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import HomeView, SearchResultsView

urlpatterns = [
        path('search/', SearchResultsView.as_view(), name='search_results'),
        path('', HomeView.as_view(), name='home'),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

