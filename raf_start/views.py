from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm # formularios incorporados de Django para manejar el registro y autenticación de usuarios
from django.contrib.auth.models import User # modelo de usuario incorporado de Django para manejar la autenticación y gestión de usuarios
from django.contrib.auth import login, logout, authenticate # crea una sesión de usuario después de un registro exitoso
from django.db import IntegrityError # captura errores de integridad de la base de datos, como intentar crear un usuario con un nombre de usuario que ya existe
from rent_a_flick.forms import FlickForm, PlatformForm, AvailabilityForm
from raf_start.models import Flick, Platform, Availability, Genre
from httpx import request

# Create your views here.
def home(request):
    return render(request, 'home.html')

# vista de formulario de registro
def signup(request):

    if request.method == 'GET': # consulta de datos
        return render(request, 'signup.html', {
            'form': UserCreationForm()
        }) # muestra un formulario vacío para GET
    
    if request.method == 'POST': # envío de datos
        #form = UserCreationForm(request.POST)

        if request.POST['password1'] == request.POST['password2']: # verifica que las contraseñas coincidan
        #if form.is_valid():
            try: # captura de errores de almacenamiento de datos de usuario
                user = User.objects.create_user(username = request.POST['username'], password = request.POST['password1']) # crea un nuevo usuario con los datos del formulario
                user.save() # guarda el nuevo usuario en la base de datos
                login(request, user) # inicia sesión para el nuevo usuario
                return redirect('dashboard') # redirige al dashboard después de un registro exitoso
            
            except IntegrityError: # renderiza de vuelta al formulario de registro con un mensaje de error si el nombre de usuario ya existe
                return render(request, 'signup.html', {
                    'form': UserCreationForm(),
                    'error': "Error. Username already exists."
                }) # muestra un formulario vacío para GET
            
        return render(request, 'signup.html', { # renderiza de vuelta al formulario de registro con un mensaje de error si las contraseñas no coinciden
            'form': UserCreationForm(),
            'error': "Error. Passwords do not match."
        }) # muestra un formulario vacío para GET
    
# vista del dashboard del usuario
def dashboard(request):
    return render(request, 'dashboard.html')

# cierre de sesión y redirección a la página de inicio
def signout(request):
    logout(request)
    return redirect('home')

# inicio de sesión
def signin(request):

    if request.method == 'GET': # consulta de datos
        return render(request, 'signin.html', {
            'form': AuthenticationForm()
        }) # muestra un formulario vacío para GET
    
    if request.method == 'POST': # envío de datos
        
        user = authenticate(request, username = request.POST['username'], password = request.POST['password']) # autentica al usuario con los datos del formulario

        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': "Error. Username or password is incorrect."
            })
        
        else:
            login(request, user) # inicia sesión para el usuario autenticado
            return redirect('dashboard')

# vista de la lista de películas
def flicks(request):
    flicks = Flick.objects.filter(user = request.user) # obtiene todas las películas asociadas al usuario actual
    return render(request, 'flicks.html', {'flicks': flicks}) # renderiza la plantilla de la lista de películas con las películas del usuario actual

# vista de creación de película
def add_flick(request):

    if request.method == 'GET':
        return render(request, 'add_flick.html', {'flick_form': FlickForm})
    
    else:
        try:
            flick_form = FlickForm(request.POST)
            new_flick = flick_form.save(commit=False) # crea una instancia del modelo Flick pero no la guarda en la base de datos aún
            new_flick.user = request.user # asigna el usuario actual como propietario de la película
            new_flick.save() # guarda la nueva película en la base de datos
            return redirect('flicks')
        
        except ValueError:
            return render(request, 'add_flick.html', {
                'flick_form': FlickForm,
                'error': "Error. Invalid data entered."
            })

# vista de detalle de película   
def flick_detail(request, flick_id):
    flick = get_object_or_404(Flick, pk=flick_id) # obtiene la película con el ID especificado
    return render(request, 'flick_detail.html', {'flick': flick}) # renderiza la plantilla de detalle de película con la película obtenida

# vista de actualización de película
def flick_update(request, flick_id):
    flick = get_object_or_404(Flick, pk=flick_id) # obtiene la película con el ID especificado

    if request.method == 'GET':
        flick_form = FlickForm(instance=flick) # crea un formulario prellenado con los datos de la película
        return render(request, 'flick_update.html', {'flick_form': flick_form, 'flick': flick})
    
    else:
        try:
            flick_form = FlickForm(request.POST, instance=flick) # actualiza la instancia del modelo Flick con los datos del formulario
            flick_form.save() # guarda los cambios en la base de datos
            return redirect('flicks')
        
        except ValueError:
            return render(request, 'flick_update.html', {
                'flick_form': FlickForm(instance=flick),
                'flick': flick,
                'error': "Error. Invalid data entered."
            })

# vista de la lista de plataformas
def platforms(request):
    return render(request, 'platforms.html')

# vista de creación de plataforma
def add_platform(request):

    if request.method == 'GET':
        return render(request, 'add_platform.html', {'platform_form': PlatformForm})
    
    else:
        try:
            platform_form = PlatformForm(request.POST)
            platform_form.save() # crea y guarda una nueva plataforma en la base de datos
            return redirect('platforms')
        
        except ValueError:
            return render(request, 'add_platform.html', {
                'platform_form': PlatformForm,
                'error': "Error. Invalid data entered."
            })
        
# vista de detalle de plataforma
def platform_detail(request, platform_id):
    platform = get_object_or_404(Platform, pk=platform_id) # obtiene la plataforma con el ID especificado
    return render(request, 'platform_detail.html', {'platform': platform}) # renderiza la plantilla de detalle de plataforma con la plataforma obtenida

# vista de actualización de plataforma
def platform_update(request, platform_id):
    platform = get_object_or_404(Platform, pk=platform_id) # obtiene la plataforma con el ID especificado

    if request.method == 'GET':
        platform_form = PlatformForm(instance=platform) # crea un formulario prellenado con los datos de la plataforma
        return render(request, 'platform_update.html', {'platform_form': platform_form, 'platform': platform})
    
    else:
        try:
            platform_form = PlatformForm(request.POST, instance=platform) # actualiza la instancia del modelo Platform con los datos del formulario
            platform_form.save() # guarda los cambios en la base de datos
            return redirect('platforms')
        
        except ValueError:
            return render(request, 'platform_update.html', {
                'platform_form': PlatformForm(instance=platform),
                'platform': platform,
                'error': "Error. Invalid data entered."
            })

# vista de la lista de disponibilidades
def availabilities(request):
    return render(request, 'availabilities.html')

# vista de creación de disponibilidad
def add_availability(request):

    if request.method == 'GET':
        return render(request, 'add_availability.html', {'availability_form': AvailabilityForm})
    
    else:
        try:
            availability_form = AvailabilityForm(request.POST)
            availability_form.save() # crea y guarda una nueva disponibilidad en la base de datos
            return redirect('availabilities')
        
        except ValueError:
            return render(request, 'add_availability.html', {
                'availability_form': AvailabilityForm,
                'error': "Error. Invalid data entered."
            })
