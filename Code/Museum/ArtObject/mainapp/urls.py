from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name = ''),
    path('Explore/', views.Explore, name = 'Explore'),
    path('Explore/ExhibitDetails/<path:ExhibitName>', views.ExhibitDetails, name = 'ExhibitName'),
    path('ArtCollections/BorrowedDetails/<path:CollName>', views.BorrowedDetails, name = 'CollName'),
    path('ArtPieces/', views.ArtPieces, name = 'ArtPieces'),
    path('ArtPieces/ArtPieceDetails/<path:IdNo>', views.ArtPieceDetails, name = 'IdNo'),
    path('ArtCollections/', views.ArtCollections, name = 'ArtCollections'),
]

htmx_urlpatterns = [
     path('search-art/', views.search_art, name = 'search-art'),
     path('ArtPieces/search-art/', views.search_art, name = 'search-art'),
     path('Explore/search-exhibit/', views.search_exhibit, name = 'search-exhibit'),
     path('ArtCollections/search-collections/', views.search_collections, name = 'search-collections'),
]

urlpatterns += htmx_urlpatterns