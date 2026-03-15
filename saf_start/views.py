from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from sort_a_flix.forms import FlixForm, PlatformForm, AvailabilityForm, SigninForm, SignupForm
from saf_start.models import Flix, Platform, Availability, Genre
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'home.html')


# cierre de sesión y redirección a la página de inicio
@login_required
def signout(request):
    logout(request)
    return redirect('home')


# inicio de sesión
def signin(request):

    if request.method == 'GET':
        return render(request, 'userauth/signin.html', {'form': SigninForm})

    if request.method == 'POST':
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])

        if user is None:
            return render(request, 'userauth/signin.html', {
                'form': SigninForm,
                'error': "Error. Username or password is incorrect."
            })
        else:
            login(request, user)
            return redirect('dashboard')


# vista de formulario de registro
def signup(request):

    if request.method == 'GET':
        return render(request, 'userauth/signup.html', {'form': SignupForm})

    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'],
                    password=request.POST['password1']
                )
                user.save()
                login(request, user)
                return redirect('dashboard')
            except IntegrityError:
                return render(request, 'userauth/signup.html', {
                    'form': SignupForm,
                    'error': "Error. Username already exists."
                })

        return render(request, 'userauth/signup.html', {
            'form': SignupForm,
            'error': "Error. Passwords do not match."
        })


# vista del dashboard del usuario
@login_required
def dashboard(request):
    flixs = Flix.objects.filter(user=request.user)

    return render(request, 'dashboard.html', {
        'total':                  flixs.count(),
        'watched':                flixs.filter(status='Watched').count(),
        'watching':               flixs.filter(status='Watching').count(),
        'watch':                  flixs.filter(status='Watch').count(),
        'platform_count':         Platform.objects.filter(user=request.user).count(),
        'availability_count':     Availability.objects.filter(user=request.user).count(),
        'recent_flixs':           flixs.order_by('-id')[:5],
        'recent_platforms':       Platform.objects.filter(user=request.user).order_by('-id')[:5],
        'recent_availabilities':  Availability.objects.filter(user=request.user)
                                      .select_related('flix', 'platform').order_by('-id')[:5],
    })


# ── Flixs ─────────────────────────────────────────────────

# vista de la lista de películas
@login_required
def flixs(request):
    flixs = Flix.objects.filter(user=request.user)
    return render(request, 'flix/flixs.html', {'flixs': flixs})


# vista de creación de película
@login_required
def add_flix(request):

    if request.method == 'GET':
        return render(request, 'flix/add_flix.html', {'flix_form': FlixForm})

    try:
        flix_form = FlixForm(request.POST, request.FILES)
        new_flix = flix_form.save(commit=False)
        new_flix.user = request.user
        new_flix.save()
        flix_form.save_m2m()  # guarda la relación ManyToMany de géneros
        return redirect('flixs')
    except ValueError:
        return render(request, 'flix/add_flix.html', {
            'flix_form': FlixForm,
            'error': "Error. Invalid data entered."
        })


# vista de detalle de película
@login_required
def flix_detail(request, flix_id):
    flix = get_object_or_404(Flix, pk=flix_id)
    return render(request, 'flix/flix_detail.html', {'flix': flix})


# vista de actualización de película
@login_required
def flix_update(request, flix_id):
    flix = get_object_or_404(Flix, pk=flix_id)

    if request.method == 'GET':
        # instance=flix precarga todos los campos, incluidos los géneros (ManyToMany)
        flix_form = FlixForm(instance=flix)
        return render(request, 'flix/flix_update.html', {'flix_form': flix_form, 'flix': flix})

    try:
        # instance=flix actualiza el registro existente en lugar de crear uno nuevo
        flix_form = FlixForm(request.POST, request.FILES, instance=flix)
        if flix_form.is_valid():
            flix_form.save()
            return redirect('flixs')
        return render(request, 'flix/flix_update.html', {'flix_form': flix_form, 'flix': flix})
    except ValueError:
        return render(request, 'flix/flix_update.html', {
            'flix_form': FlixForm(instance=flix),
            'flix': flix,
            'error': "Error. Invalid data entered."
        })


# vista de confirmación y borrado de película
# El template muestra el formulario de confirmación encima de la página de fondo
@login_required
def flix_delete(request, flix_id):
    flix = get_object_or_404(Flix, pk=flix_id, user=request.user)  # solo el propietario puede borrar

    if request.method == 'POST':
        flix.delete()
        return redirect('flixs')

    # GET: muestra la página de confirmación pasando el flix al template
    return render(request, 'flix/flix_confirm_delete.html', {'flix': flix})


# ── Platforms ──────────────────────────────────────────────

# vista de la lista de plataformas
@login_required
def platforms(request):
    # Todos los usuarios pueden ver todas las plataformas
    platforms = Platform.objects.all().select_related('user')
    return render(request, 'platform/platforms.html', {'platforms': platforms})


# vista de creación de plataforma
@login_required
def add_platform(request):

    if request.method == 'GET':
        return render(request, 'platform/add_platform.html', {'platform_form': PlatformForm})

    try:
        platform_form = PlatformForm(request.POST, request.FILES)
        new_platform = platform_form.save(commit=False)
        new_platform.user = request.user  # asigna el usuario actual como propietario
        new_platform.save()
        return redirect('platforms')
    except ValueError:
        return render(request, 'platform/add_platform.html', {
            'platform_form': PlatformForm,
            'error': "Error. Invalid data entered."
        })


# vista de detalle de plataforma
@login_required
def platform_detail(request, platform_id):
    platform = get_object_or_404(Platform, pk=platform_id)
    availabilities = Availability.objects.filter(
        platform=platform, user=request.user
    ).select_related('flix')
    return render(request, 'platform/platform_detail.html', {
        'platform': platform,
        'availabilities': availabilities,
    })


# vista de actualización de plataforma
@login_required
def platform_update(request, platform_id):
    # Solo el propietario puede editar la plataforma
    platform = get_object_or_404(Platform, pk=platform_id, user=request.user)

    if request.method == 'GET':
        platform_form = PlatformForm(instance=platform)
        return render(request, 'platform/platform_update.html', {
            'platform_form': platform_form,
            'platform': platform,
        })

    try:
        platform_form = PlatformForm(request.POST, request.FILES, instance=platform)
        if platform_form.is_valid():
            platform_form.save()
            return redirect('platforms')
        return render(request, 'platform/platform_update.html', {
            'platform_form': platform_form,
            'platform': platform,
        })
    except ValueError:
        return render(request, 'platform/platform_update.html', {
            'platform_form': PlatformForm(instance=platform),
            'platform': platform,
            'error': "Error. Invalid data entered."
        })


# ── Availabilities ───────────────────────────────────────

# vista de la lista de disponibilidades
@login_required
def availabilities(request):
    # Solo el usuario que la creó puede ver sus entradas
    avs = Availability.objects.filter(user=request.user).select_related('flix', 'platform')
    return render(request, 'availability/availabilities.html', {'availabilities': avs})


# vista de creación de disponibilidad
@login_required
def add_availability(request):

    # películas del usuario actual — se usan para filtrar el desplegable "flix"
    user_flixs = Flix.objects.filter(user=request.user)
 
    if request.method == 'GET':
        form = AvailabilityForm()
        form.fields['flix'].queryset = user_flixs  # solo sus películas en el select
        return render(request, 'availability/add_availability.html', {'availability_form': form})
    
    if request.method == 'POST':
 
        form = AvailabilityForm(request.POST)
        form.fields['flix'].queryset = user_flixs  # mismo filtro para la validación     

        try:
            availability_form = AvailabilityForm(request.POST)
            new_av = availability_form.save(commit=False)
            new_av.user = request.user  # asigna el usuario actual como propietario
            new_av.save()
            return redirect('availabilities')
        except ValueError:
            return render(request, 'availability/add_availability.html', {
                'availability_form': AvailabilityForm,
                'error': "Error. Invalid data entered."
            })


# vista de actualización de disponibilidad
@login_required
def availability_update(request, availability_id):
    # Solo el propietario puede editar su entrada
    availability = get_object_or_404(Availability, pk=availability_id, user=request.user)

    if request.method == 'GET':
        availability_form = AvailabilityForm(instance=availability)
        return render(request, 'availability/availability_update.html', {
            'availability_form': availability_form,
            'availability': availability,
        })

    try:
        availability_form = AvailabilityForm(request.POST, instance=availability)
        if availability_form.is_valid():
            availability_form.save()
            return redirect('availabilities')
        return render(request, 'availability/availability_update.html', {
            'availability_form': availability_form,
            'availability': availability,
        })
    except ValueError:
        return render(request, 'availability/availability_update.html', {
            'availability_form': AvailabilityForm(instance=availability),
            'availability': availability,
            'error': "Error. Invalid data entered."
        })


# vista de confirmación y borrado de disponibilidad
#
# Mismo patrón que flix_delete: GET muestra confirmación, POST ejecuta el borrado.
@login_required
def availability_delete(request, availability_id):
    availability = get_object_or_404(Availability, pk=availability_id, user=request.user)

    if request.method == 'POST':
        availability.delete()
        return redirect('availabilities')

    return render(request, 'availability/availability_confirm_delete.html', {'availability': availability})
