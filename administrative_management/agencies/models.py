from django.db import models

class Agency(models.Model):
    name = models.CharField(max_length=30)
    idAgency = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    state = models.CharField(max_length=20)
    cp = models.CharField(max_length=10)
