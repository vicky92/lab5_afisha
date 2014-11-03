# -*- coding: utf-8 -*-
from django.db import models


# Create your models here.

class Cinema(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    
    
class Film(models.Model):
    name = models.CharField(max_length=100)
    about = models.CharField(max_length=500)
   


class Poster(models.Model):
    viewDate = models.DateTimeField()
    cinemaId = models.ForeignKey(Cinema)
    filmId   = models.ForeignKey(Film)
    