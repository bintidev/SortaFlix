from django.contrib import admin
from.models import Flick, Platform, Availability, Genre

# Register your models here.
admin.site.register(Flick)
admin.site.register(Platform)
admin.site.register(Availability)
admin.site.register(Genre)

class PlatformAdmin(admin.ModelAdmin):
    readonly_fields = ('parent')

class AvailabilityAdmin(admin.ModelAdmin):
    readonly_fields = ('flick')

class GenreAdmin(admin.ModelAdmin):
    readonly_fields = ('name')