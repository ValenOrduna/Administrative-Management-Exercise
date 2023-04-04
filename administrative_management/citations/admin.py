from django.contrib import admin

from citations.models import Citation

# Configuracion del modelo admin Citation
class CitationAdmin(admin.ModelAdmin):
    list_display = ('violationDate','violationTime','route','county','city','oln','oln_number','license_class','cdl','name','dob','gender','hair_color','eye_color','height','address','city','state','zip_code','phone','vin','color','year','make','model','crash','passengers','spanish_speaker','in_car_video','body_camera','school_zone','construction_zone','workers_present','violations','officer')
    search_fields = ('violationDate','violationTime','route','county','city','oln','oln_number','license_class','cdl','name','dob','gender','hair_color','eye_color','height','address','city','state','zip_code','phone','vin','color','year','make','model','crash','passengers','spanish_speaker','in_car_video','body_camera','school_zone','construction_zone','workers_present','violations','officer')
    
admin.site.register(Citation,CitationAdmin)
