from django.contrib import admin
from officers.models import Officer

class OfficerAdmin(admin.ModelAdmin):
    list_display = ('name','badge','agency')
    search_fields = ('name','badge','agency')
    
admin.site.register(Officer,OfficerAdmin)