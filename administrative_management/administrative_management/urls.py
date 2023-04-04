from django.contrib import admin
from django.urls import path
from login.views import login
from home.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login',login,name='login'),
    path('',home,name='home'),
]
