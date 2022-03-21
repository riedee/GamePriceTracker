from django.urls import path
from .views import HomeView, SearchResultsView, GameView, VendorPageView, VendorView

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    path('search/', SearchResultsView, name='search_results'),
    path('results/<str:info>', GameView, name='game'),
    path('temporary', VendorView, name='vendor'),
        
    path('', HomeView.as_view(), name='home'),
    path('#vendors', VendorPageView.as_view(), name='vendorpage'),
]

