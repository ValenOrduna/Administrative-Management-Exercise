from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login as auth_login

# Vista Login

# Decorador csrf 
@csrf_protect
def login(request):
    # Verificamos si el usuario ya esta logueado, si esta logueado lo redireccionamos al home
    if request.user.is_authenticated:
        return redirect('/')
    # Metodo POST
    if request.method == 'POST':
        # Extraemos los datos del formulario
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Autenticamos si el usuario esta creado
        user = authenticate(request,username=username, password=password)
        # Si el usuario esta creado logueamos, sino generamos alerta
        if user is not None:
            auth_login(request,user)
            return redirect('/')
        return render(request, 'login.html',{'alert':'Las credenciales de inicio de sesión no son válidas. Inténtelo de nuevo.'})
    return render(request,'login.html')
