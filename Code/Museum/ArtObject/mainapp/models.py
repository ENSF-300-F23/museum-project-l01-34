from typing import Any
from django.db import models

class Artist(models.Model):
    ArtistName = models.CharField(primary_key = True, max_length = 40)
    DateBorn = models.IntegerField(null = True, blank = True)
    DateDied = models.IntegerField(null = True, blank = True)
    CountryOfOrigin = models.CharField(max_length = 20, blank = True)
    MainStyle = models.CharField(max_length = 20, blank = True)
    Epoch = models.CharField(max_length = 20, blank = True)
    ArtistDesc = models.CharField(max_length = 60, blank = True) 
    
    def __str__(self):
        return self.ArtistName
    
class Exhibition(models.Model):
    ExhibitName = models.CharField(primary_key = True, max_length = 80)
    StartDate = models.DateField()
    EndDate = models.DateField()
    
    def __str__(self):
        return self.ExhibitName
    
class ArtObject(models.Model):
    IdNo = models.CharField(primary_key = True, max_length = 7)
    Title = models.CharField(max_length = 60, default = 'Unknown')
    YearMade = models.IntegerField(null = True)
    Origin = models.CharField(max_length = 20, blank = True)
    Style = models.CharField(max_length = 20, blank = True)
    Epoch = models.CharField(max_length = 20, blank = True)
    ArtDesc = models.CharField(max_length = 60, blank = True)
    
    ExhibitName = models.ForeignKey("Exhibition", on_delete = models.CASCADE, default = None, blank = True, null = True)  
    ArtistName = models.ForeignKey("Artist", on_delete = models.CASCADE, default = None, blank = True, null = True)
    
    def __str__(self):
        return self.IdNo
    
class Painting(models.Model):
    IdNo = models.ForeignKey("ArtObject", primary_key = True, on_delete = models.CASCADE)
    PaintType = models.CharField(max_length = 15, blank = True)
    DrawnOn = models.CharField(max_length = 15, blank = True)


    
class SculptureOrStatue(models.Model):
    IdNo = models.ForeignKey("ArtObject", primary_key = True, on_delete = models.CASCADE)
    Material = models.CharField(max_length = 50, null = True, blank = True)
    Height = models.DecimalField(max_digits = 10, decimal_places = 4, null = True, blank = True)
    Weight = models.DecimalField(max_digits = 10, decimal_places = 4, null = True, blank = True)
    
    
class Other(models.Model):
    IdNo = models.ForeignKey("ArtObject", primary_key = True, on_delete = models.CASCADE)
    ArtType = models.CharField(max_length = 15, blank = True)
    
    
class Collection(models.Model):
    CollName = models.CharField(max_length = 30, primary_key = True)
    CollType = models.CharField(max_length = 15)
    Phone = models.CharField(max_length = 15)
    ContactPerson = models.CharField(max_length = 20, blank = True)
    Epoch = models.CharField(max_length = 20, blank = True)
    CollDesc = models.CharField(max_length = 100, blank = True)
    
    
    
class PermanentCollection(models.Model):
    IdNo = models.ForeignKey("ArtObject", primary_key = True, on_delete = models.CASCADE)
    DateAquired = models.DateField()
    PcollStatus = models.CharField(max_length = 10)
    Cost = models.DecimalField(max_digits = 19, decimal_places = 4, null = True)
    
    
class Borrowed(models.Model):
    IdNo = models.ForeignKey("ArtObject", primary_key = True, on_delete = models.CASCADE)
    CollName = models.ForeignKey("Collection", on_delete = models.CASCADE)
    DateBorrowed = models.DateField()
    DateReturned = models.DateField()
    
    
   
