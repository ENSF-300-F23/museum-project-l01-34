from django.http import HttpResponse
from django.template import loader
from .models import *

def Home(request):
  template = loader.get_template('Home.html')
  context = {'Home' : 'Home'}
  return HttpResponse(template.render(context, request))

def Explore(request):
  exibits = Exhibition.objects.all().values()
  template = loader.get_template('Explore.html')
  context = {
    'Exhibits' : exibits,
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
