from django.db import models
from division.models import Divisions
# Create your models here.

class Districts(models.Model):
    districName = models.CharField(max_length=20)
    divisionID = models.ForeignKey(Divisions, on_delete=models.CASCADE)
