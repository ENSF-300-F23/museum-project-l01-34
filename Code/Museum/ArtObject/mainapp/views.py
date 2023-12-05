import datetime
from django.http import HttpResponse
from django.template import loader
from django.db.models import Q
from .models import *

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
  if request.GET.get('search'):
    sq = request.GET.get('search')
  exibits = Exhibition.objects.filter(Q(ExhibitName__icontains = sq))
  template = loader.get_template('Explore.html')
  context = {
    'Exhibits' : exibits,
  }
  return HttpResponse(template.render(context, request))

def ArtPieces(request):
  sq = ''
  if request.GET.get('search'):
    sq = request.GET.get('search')
  ArtObjects = ArtObject.objects.filter(Q(Title__icontains = sq))
  template = loader.get_template('ArtPieces.html')
  context = {
    'ArtObjects' : ArtObjects,
  }
  return HttpResponse(template.render(context, request))

def ArtPieceDetails(request, IdNo):
   artPiece = ArtObject.objects.get(IdNo = IdNo)
   template = loader.get_template('ArtPieceDetails.html')
   context = {
     'ArtPiece' : artPiece
   }
   return HttpResponse(template.render(context, request))

def ExhibitDetails(request, ExhibitName):
  exhibit = Exhibition.objects.get(ExhibitName = ExhibitName)
  artobjects = DisplayedIn.objects.filter(ExhibitName = ExhibitName)
  template = loader.get_template('ExhibitDetails.html')
  context = {
    'Exhibit' : exhibit,
    'ArtObjects' : artobjects,
  }

  return HttpResponse(template.render(context, request))

def search_art(request):
  currentUrl = request.path
  search_text = request.GET.get('search')
  
  if(currentUrl == '/search-art/' or '/ArtPieces/search-art/'):
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
      Q(ArtistName = search_text) 
      ).distinct()
    exhibitObjects = DisplayedIn.objects.filter(Q(ExhibitName = search_text)).values_list("IdNo", flat = True)
    results = results.union(ArtObject.objects.filter(IdNo__in = exhibitObjects).distinct())
  else:
    results = ArtObject.objects.filter(Title__icontains = search_text)
    
  objectIds = results.values_list('IdNo', flat = True)
  
  paintings = Painting.objects.filter(IdNo__in = objectIds).values_list('IdNo', flat = True)
  paintings = ArtObject.objects.filter(IdNo__in = paintings)
  
  sculpsOrStats = SculptureOrStatue.objects.filter(IdNo__in = objectIds).values_list('IdNo', flat = True)
  sculpsOrStats = ArtObject.objects.filter(IdNo__in = sculpsOrStats)
  
  others = Other.objects.filter(IdNo__in = objectIds).values_list('IdNo', flat = True)
  others = ArtObject.objects.filter(IdNo__in = others)
  if(currentUrl == '/ArtPieces/search-art/'):
    template = loader.get_template('partials/search-multiartresults.html')
  else:
    template = loader.get_template('partials/search-artresults.html')

  context = {
    'ArtObjects' : results,
    'Paintings' : paintings,
    'SculpsOrStats' : sculpsOrStats,
    'Others' : others
    }
  return HttpResponse(template.render(context, request))

def search_exhibit(request):
  search_text = request.GET.get('search')
  try:
    search_date = datetime.datetime.strptime(search_text, '%Y-%m-%d').date()
  except:
    search_date = None
     
  results = Exhibition.objects.filter(
    Q(ExhibitName__icontains = search_text) |
    Q(StartDate = search_date) |
    Q(EndDate = search_date)
    ).distinct()
  template = loader.get_template('partials/search-exhibitresults.html')
  context = {
    'Exhibits' : results
  }
  return HttpResponse(template.render(context, request))
