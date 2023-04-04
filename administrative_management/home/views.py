from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from officers.models import Officer
from agencies.models import Agency
from home.forms.officerForm import OfficerForm

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
            # Si se encuentra el usuario se renderiza el template sino reddiccionara a login
            try:
                findUser = Officer.objects.get(name=user) 
                return render(request,'index.html',{'profile':findUser} )
            except Exception as e:
                return redirect('/login')
    # Comprobamos si el usuario es un Clerk
    if request.user.groups.filter(name='Clerk').exists():
            user = request.user.username
            user = user.replace('_',' ')
            user = user.title()
            try:
                findUser = Officer.objects.get(name=user)
                filterAgency = Officer.objects.filter(agency=findUser.agency)  
                return render(request,'index.html',{'profiles':filterAgency} )
            except Exception as e:
                return redirect('/login')
    return render(request, 'index.html')


# Ruta Actualizar Officer
@csrf_protect
@login_required(login_url='/login')
def updateProfile(request,idOfficer):
    # Verificamos si el usuario esta autentificado
    if request.user.is_authenticated:
        # Verificamos si el metodo es POST
        if request.method == 'POST':
            try:
                # Actualizamos los datos recibios y los validamos
                update = request.POST.dict()
                update['agency'] = Agency.objects.get(name=update['agency'])
                form = OfficerForm(update)
                if form.is_valid():
                    Officer.objects.filter(pk=idOfficer).update(**form.cleaned_data)
                    return redirect('/')
                return redirect('/')
            except Exception as e:
                return redirect('/')
        return redirect('/')           