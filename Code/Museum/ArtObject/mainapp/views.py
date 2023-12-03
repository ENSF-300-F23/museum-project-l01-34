from django.http import HttpResponse
from django.template import loader
from django.db.models import Q
from .models import *
from django.views.decorators.csrf import csrf_protect

def Home(request):
  sq = ''
  if request.GET.get('searchQuery'):
    sq = request.GET.get('searchQuery')
  ArtObjects = ArtObject.objects.filter(Q(Title__icontains = sq))
  template = loader.get_template('Home.html')
  context = {
    'Home' : 'Home',
    'ArtObjects' : ArtObjects
  }
  return HttpResponse(template.render(context, request))

def Explore(request):
  sq = ''
  if request.GET.get('searchQuery'):
    sq = request.GET.get('searchQuery')
  exibits = Exhibition.objects.filter(Q(ExhibitName__icontains = sq))
  template = loader.get_template('Explore.html')
  context = {
    'Exhibits' : exibits,
  }
  return HttpResponse(template.render(context, request))

def ArtPieces(request):
  sq = ''
  if request.GET.get('searchQuery'):
    sq = request.GET.get('searchQuery')
  ArtObjects = ArtObject.objects.filter(Q(Title__icontains = sq))
  template = loader.get_template('ArtPieces.html')
  context = {
    'ArtObjects' : ArtObjects,
  }
  return HttpResponse(template.render(context, request))

def ArtPieceDetails(request, Title):
   artPiece = ArtObject.objects.get(Title = Title)
   template = loader.get_template('ArtPieceDetails.html')
   context = {
     'ArtPiece' : artPiece
   }
   return HttpResponse(template.render(context, request))

def ExhibitDetails(request, ExhibitName):
  exhibit = Exhibition.objects.get(ExhibitName = ExhibitName)
  artobjects = ArtObject.objects.filter(ExhibitName = ExhibitName)
  template = loader.get_template('ExhibitDetails.html')
  context = {
    'Exhibit' : exhibit,
    'ArtObjects' : artobjects,
  }

  return HttpResponse(template.render(context, request))


def search_art(request):
  currentUrl = request.path
  search_text = request.GET.get('search')
  
  if(currentUrl == '/search-art/'):
    try:
      searchYear = int(search_text)
    except:
      searchYear = -1
    results = ArtObject.objects.filter(
      Q(Title__icontains = search_text) |
      Q(IdNo = search_text) |
      Q(YearMade = searchYear) |
      Q(Origin__iexact = search_text) |
      Q(Style__iexact = search_text) |
      Q(Epoch__iexact = search_text) |
      Q(ArtDesc__icontains = search_text) |
      Q(ExhibitName = search_text) |
      Q(ArtistName = search_text) 
      )
  else:
    results = ArtObject.objects.filter(Title__icontains = search_text)
    
  template = loader.get_template('partials/search-artresults.html')
  context = {
    'ArtObjects' : results
  }
  return HttpResponse(template.render(context, request))

def search_exhibit(request):
  search_text = request.GET.get('search')
  
  results = Exhibition.objects.filter(
    Q(ExhibitName__icontains = search_text) |
    Q(StartDate = search_text) |
    Q(EndDate = search_text)
    )
  template = loader.get_template('partials/search-exhibitresults.html')
  context = {
    'Exhibits' : results
  }
  return HttpResponse(template.render(context, request))
