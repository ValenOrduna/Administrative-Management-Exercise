from django.db import models
from officers.models import Officer

# Modelo Multa
class Citation(models.Model):
    # Datos Citation
    violationDate = models.DateField()
    violationTime = models.TimeField()
    route = models.CharField(max_length=20)
    county = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    # Datos Pasajero
    oln = models.CharField(max_length=10)
    oln_number = models.CharField(max_length=10)
    license_class = models.CharField(max_length=10)
    cdl = models.BooleanField()
    name = models.CharField(max_length=50)
    dob = models.DateField()
    gender = models.CharField(max_length=10)
    hair_color = models.CharField(max_length=10,null=True)
    eye_color = models.CharField(max_length=10,null=True)
    height = models.CharField(max_length=8)
    address = models.CharField(max_length=50)
    city_passenger = models.CharField(max_length=50)
    state = models.CharField(max_length=10)
    zip_code = models.CharField(max_length=10)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=40)
    # Datos Auto Pasajero
    vin = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    year = models.IntegerField()
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    # Datos Factores
    crash = models.BooleanField()
    passengers = models.BooleanField()
    spanish_speaker = models.BooleanField()
    in_car_video = models.BooleanField()
    body_camera = models.BooleanField()
    school_zone = models.BooleanField()
    construction_zone = models.BooleanField()
    workers_present = models.BooleanField()
    # Datos Violaciones
    violations = models.CharField(max_length=100)
    # Datos Oficial
    officer = models.ForeignKey(Officer,on_delete=models.CASCADE)
    # Nota Oficial
    officer_note = models.CharField(max_length=100,null=True)
    
