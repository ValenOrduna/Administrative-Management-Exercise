from django.contrib import admin
from agencies.models import Agency

class AgencyAdmin(admin.ModelAdmin):
    list_display = ('name','idAgency', 'address','state','cp')
    search_fields = ('name','idAgency', 'address','state','cp')
    
admin.site.register(Agency,AgencyAdmin)
