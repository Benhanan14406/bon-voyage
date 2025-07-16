from django.db import models

# Create your models here.
class Travel(models.Model):
    currentLoc = models.CharField(max_length=1000, default="", editable=True)
    destination = models.CharField(max_length=1000, default="", editable=True)
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()
    travelTime = models.IntegerField(default=0, db_default=0, editable=True)
    travelMode = models.CharField(max_length=10, default="", editable=True)
    travelError = models.IntegerField(default=0, db_default=0, editable=True)
    tolCost = models.IntegerField(default=0, db_default=0, editable=True)