from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from home.helpers.cleanUser import cleanUser
from officers.models import Officer
from agencies.models import Agency
from citations.models import Citation
from home.forms.officerForm import OfficerForm

# Controller Home
# Validamos si el usuario ya esta logueado, sino lo redirigimos al login
@login_required(login_url='/login')
def home(request):
    # Comprobamos si el usuario es un Officer
    if request.user.groups.filter(name='Officer').exists():
            # Limpiamos el nombre del usuario para buscarlo en la base de datos
            user = cleanUser(request.user.username)
            # Si se encuentra el usuario se renderiza el template sino reddiccionara a login
            try:
                findUser = Officer.objects.get(name=user) 
                findCitations = Citation.objects.filter(officer=findUser).order_by('-id')
                return render(request,'index.html',{'profile':findUser,'citations':findCitations} )
            except Exception as e:
                return redirect('/login')
    # Comprobamos si el usuario es un Clerk
    if request.user.groups.filter(name='Clerk').exists():
            # Limpiamos el nombre del usuario para buscarlo en la base de datos
            user = cleanUser(request.user.username)
            # Si se encuentra el usuario se renderiza el template sino reddiccionara a login
            try:
                # Obtenemos el usuario
                findUser = Officer.objects.get(name=user)
                filterAgency = Officer.objects.filter(agency=findUser.agency)
                # Filtramos los oficiales que pertenecen a la agencia y filtramos las multas de esos oficiales
                filterOfficer = Officer.objects.filter(agency=findUser.agency)
                citations = Citation.objects.filter(officer__in=filterOfficer)
                return render(request,'index.html',{'profiles':filterAgency,'citations':citations} )
            except Exception as e:
                return redirect('/login')
    # Comprobamos si el usuario es un Admin
    if request.user.groups.filter(name='Admin').exists():
        findUsers = Officer.objects.filter()
        findCitations = Citation.objects.filter()
        return render(request,'index.html',{'profiles':findUsers,'citations':findCitations} )
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