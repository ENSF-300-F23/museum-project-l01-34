from django.http import HttpResponse
from django.template import loader
from django.db.models import Q
from .models import *

def Home(request):
  template = loader.get_template('Home.html')
  context = {'Home' : 'Home'}
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
  

def ExhibitDetails(request, ExhibitName):
  sq = ''
  if request.GET.get('searchQuery'):
    sq = request.GET.get('searchQuery')
  exhibit = Exhibition.objects.get(ExhibitName = ExhibitName)
  artobjects = ArtObject.objects.filter(ExhibitName = ExhibitName, Title__icontains = sq)
  template = loader.get_template('ExhibitDetails.html')
  context = {
    'Exhibit' : exhibit,
    'ArtObjects' : artobjects,
  }
  return HttpResponse(template.render(context, request))
