from django.contrib import admin
from citations.models import Citation
from officers.models import Officer
from agencies.models import Agency

# Configuracion del modelo admin Citation
class CitationAdmin(admin.ModelAdmin):
    list_display = ('violationDate','violationTime','route','county','city','oln','oln_number','license_class','cdl','name','dob','gender','hair_color','eye_color','height','address','city','state','zip_code','phone','vin','color','year','make','model','crash','passengers','spanish_speaker','in_car_video','body_camera','school_zone','construction_zone','workers_present','violations','officer')
    search_fields = ('violationDate','violationTime','route','county','city','oln','oln_number','license_class','cdl','name','dob','gender','hair_color','eye_color','height','address','city','state','zip_code','phone','vin','color','year','make','model','crash','passengers','spanish_speaker','in_car_video','body_camera','school_zone','construction_zone','workers_present','violations','officer')
    # Funcion mostrar filas
    def get_queryset(self, request):
        user = request.user.username
        user = user.replace('_',' ')
        user = user.title()
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        # Si el usuario es Oficial solamente podra cambiar su usuario
        if request.user.groups.filter(name='Officer').exists():
            try:
                officer = Officer.objects.get(name=user)
                return qs.filter(officer=officer)
            except Exception as e:
                print(e)
        if request.user.groups.filter(name='Clerk').exists():
            try:
                findUser = Officer.objects.get(name=user)
                # Filtramos los oficiales que pertenecen a la agencia y filtramos las multas de esos oficiales
                filterOfficer = Officer.objects.filter(agency=findUser.agency)
                return qs.filter(officer__in=filterOfficer)
            except Exception as e:
                print(e)
    
    
    
admin.site.register(Citation,CitationAdmin)
