from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from officers.models import Officer

# Vista Home
# Validamos si el usuario ya esta logueado, sino lo redirigimos al login
@login_required(login_url='/login')
def home(request):
    # Comprobamos si el usuario es un Officer
    if request.user.groups.filter(name='Officer').exists():
            # Limpiamos el nombre del usuario para buscarlo en la base de datos
            user = request.user.username
            user = user.replace('_',' ')
            user = user.title()
            try:
                findUser = Officer.objects.get(name=user) 
                return render(request,'index.html',{'profile':findUser} )
            except Exception as e:
                pass
            
    return render(request, 'index.html')