"""
URL configuration for rent_a_flix project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from saf_start import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('signout/', views.signout, name='signout'),
    path('signin/', views.signin, name='signin'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('flixs/', views.flixs, name='flixs'),
    path('flixs/add/', views.add_flix, name='add_flix'),
    path('flixs/<int:flix_id>/detail/', views.flix_detail, name='flix_detail'),
    path('flixs/<int:flix_id>/update/', views.flix_update, name='flix_update'),
    path('flixs/<int:flix_id>/delete/', views.flix_delete, name='flix_delete'),
    path('platforms/', views.platforms, name='platforms'),
    path('platforms/add/', views.add_platform, name='add_platform'),
    path('platforms/<int:platform_id>/detail/', views.platform_detail, name='platform_detail'),
    path('platforms/<int:platform_id>/update/', views.platform_update, name='platform_update'),
    path('availabilities/', views.availabilities, name='availabilities'),
    path('availabilities/add/', views.add_availability, name='add_availability'),
    path('availabilities/<int:availability_id>/delete', views.availability_delete, name='availability_delete'),
]

# Servir archivos media en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)