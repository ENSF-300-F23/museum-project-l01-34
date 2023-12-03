from django.contrib.admin import AdminSite
from django.contrib import admin
from .models import *

AdminSite.site_header = "Museum Administration"

class ArtistDisplay(admin.ModelAdmin):
    list_display = ("ArtistName", "DateBorn", "DateDied", "CountryOfOrigin", "MainStyle", "Epoch", "ArtistDesc") 
admin.site.register(Artist, ArtistDisplay)

class ExhibitionDisplay(admin.ModelAdmin):
    list_display = ("ExhibitName", "StartDate", "EndDate")
admin.site.register(Exhibition, ExhibitionDisplay)

class ArtObjectDisplay(admin.ModelAdmin):
    list_display = ("IdNo", "Title", "YearMade", "Origin", "Style", "Epoch", "ArtDesc")
admin.site.register(ArtObject, ArtObjectDisplay)

class PaintingDisplay(admin.ModelAdmin):
    list_display = ("IdNo", "PaintType", "DrawnOn")
admin.site.register(Painting, PaintingDisplay)

class OtherDisplay(admin.ModelAdmin):
    list_display = ("IdNo", "ArtType")
admin.site.register(Other, OtherDisplay)

class SculptureOrStatueDisplay(admin.ModelAdmin):
    list_display = ("IdNo", "Material", "Height", "Weight")
admin.site.register(SculptureOrStatue,SculptureOrStatueDisplay)

class CollectionDisplay(admin.ModelAdmin):
    list_display = ("CollName", "CollType", "Phone", "ContactPerson", "Epoch", "CollDesc")
admin.site.register(Collection)

class PermanentCollectionDisplay(admin.ModelAdmin):
    list_display = ("IdNo", "DateAquired", "PcollStatus", "Cost")
admin.site.register(PermanentCollection, PermanentCollectionDisplay)

class BorrowedDisplay(admin.ModelAdmin):
    list_display = ("IdNo", "CollName", "DateBorrowed", "DateReturned")
admin.site.register(Borrowed, BorrowedDisplay)