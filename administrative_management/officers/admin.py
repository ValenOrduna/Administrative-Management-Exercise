from django.contrib import admin
from officers.models import Officer
from agencies.models import Agency
class OfficerAdmin(admin.ModelAdmin):
    list_display = ('name','badge','agency')
    search_fields = ('name','badge','agency')
    
    # Configuracion del las opciones de agencias
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        user = request.user.username
        user = user.replace('_',' ')
        user = user.title()
        # Validamos el rol del usuario
        if request.user.groups.filter(name='Clerk').exists():
            # Realizamos query y obtenemos la agencia del usuario
            qs = super().get_queryset(request)
            try:
                officer = qs.get(name=user)
                officerAgency = officer.agency
                if db_field.name == "agency":
                    # Filtramos las opciones con el id de la agencia asociada al usuario
                    kwargs["queryset"] = Agency.objects.filter(pk=officerAgency.id)
            
            except Exception as e:
                print(e)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    # Funcion mostrar filas
    def get_queryset(self, request):
        user = request.user.username
        user = user.replace('_',' ')
        user = user.title()
        qs = super().get_queryset(request)
        # Si el usuario es Oficial solamente podra cambiar su usuario
        if request.user.groups.filter(name='Officer').exists():
            return qs.filter(name=user)
        if request.user.groups.filter(name='Clerk').exists():
            try:
                user = qs.get(name=user)
                return qs.filter(agency=user.agency)
            except Exception as e:
                return qs
        if request.user.groups.filter(name='Admin').exists():
            return qs
admin.site.register(Officer,OfficerAdmin)