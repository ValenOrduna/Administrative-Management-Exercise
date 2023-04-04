from django.contrib import admin
from django.urls import path
from login.views import login
from home.views import *
from citations.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login',login,name='login'),
    path('',home,name='home'),
    path('profile/update/<int:idOfficer>',updateProfile,name='updateProfile'),
    path('citation/<int:idCitation>',informationCitation,name='informationCitation'),
    path('citation/create',createCitation,name='createCitation'),
]
