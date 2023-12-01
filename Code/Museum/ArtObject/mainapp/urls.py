from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name = ''),
    path('Explore/', views.Explore, name = 'Explore'),
    path('Explore/ExhibitDetails/<path:ExhibitName>', views.ExhibitDetails, name = 'ExhibitName'),
]