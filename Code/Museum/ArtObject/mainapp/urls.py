from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name = ''),
    path('Explore/', views.Explore, name = 'Explore'),
    path('Explore/ExhibitDetails/<path:ExhibitName>', views.ExhibitDetails, name = 'ExhibitName'),
    path('ArtPieces/', views.ArtPieces, name = 'ArtPieces'),
    path('ArtPieces/ArtPieceDetails/<path:Title>', views.ArtPieceDetails, name = 'Title'),
]

htmx_urlpatterns = [
     path('search-art/', views.search_art, name = 'search-art'),
     path('ArtPieces/search-art/', views.search_art, name = 'search-art'),
     path('Explore/search-exhibit/', views.search_exhibit, name = 'search-exhibit'),
]

urlpatterns += htmx_urlpatterns