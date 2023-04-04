from django.db import models
from agencies.models import Agency

class Officer(models.Model):
    name = models.CharField(max_length=30)
    dni = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    badge = models.CharField(max_length=20,unique=True)
    agency = models.ForeignKey(Agency,on_delete=models.CASCADE)
