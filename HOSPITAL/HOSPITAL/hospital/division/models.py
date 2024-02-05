from django.db import models

# Create your models here.


class Divisions(models.Model):
    divisionName = models.CharField(max_length=20)

