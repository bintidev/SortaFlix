from django.db import models
from django.contrib.auth.models import User

# Create your models here.
'''flick: portada, titulo, director, año, género, puntuación, sinopsis, disponibilidad'''
'''flick_user: username, email, name, password, historial de alquileres'''
'''alquiler: usuario, película, fecha de alquiler, fecha de devolución'''
'''género: nombre, descripción'''

class Genre(models.Model):

    id = models.AutoField(primary_key=True, verbose_name="Genre ID")
    name = models.CharField(max_length=100, verbose_name="Name", null=False)

    def __str__(self):
        return self.name

class Flick(models.Model):

    id = models.AutoField(primary_key=True, verbose_name="Flick ID")
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    cover_image = models.ImageField(upload_to='covers/', verbose_name="Cover Image", default='covers/default.jpg', null=True, blank=True)
    title = models.CharField(max_length=100, verbose_name="Title", null=False)
    director = models.CharField(max_length=100, verbose_name="Director", default="Unknown", null=True, blank=True)
    year = models.IntegerField(verbose_name="Year", default=2000, null=False)
    genres = models.ManyToManyField(Genre)
    rating = models.FloatField(verbose_name="Rating", default=0.0, null=True, blank=True)
    duration = models.IntegerField(verbose_name="Duration", default=120)
    synopsis = models.TextField(verbose_name="Synopsis", default="No synopsis available.", null=True, blank=True)
    status = models.CharField(max_length=20, choices=[('Watched', 'Watched'), ('Watching', 'Watching'), ('Watch', 'Watch')], default='Watch')

    def __str__(self):
        return self.title

class Platform(models.Model):

    id = models.AutoField(primary_key=True, verbose_name="Platform ID")
    name = models.CharField(max_length=100, verbose_name="Platform Name", null=False)
    logo = models.ImageField(upload_to='platform_logos/', verbose_name="Platform Logo", default='platform_logos/default.png', null=True, blank=True)
    parent = models.CharField(max_length=100, verbose_name="Parent Company", null=True, blank=True)
    areas_served = models.CharField(max_length=200, verbose_name="Areas Served", null=True, blank=True)
    delivery_type = models.CharField(max_length=100, verbose_name="Delivery Type", choices=[
                                        ('Subscription Video on Demand', 'Subscription Video on Demand'),
                                        ('Live TV Streaming', 'Live TV Streaming'),
                                        ('Ad Free Streaming', 'Ad Free Streaming')
                                    ], default='Subscription Video on Demand')
    url = models.CharField(max_length=200, verbose_name="URL", null=True, blank=True, default='')
    description = models.TextField(verbose_name="Description", default="No description yet.", null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None) # recomendaciones de plataformas de otros usuarios, visibilidad pública

    def __str__(self):
        return self.name
    
class Availability(models.Model):
    
    id = models.AutoField(primary_key=True, verbose_name="Availability ID")
    flick = models.ForeignKey(Flick, on_delete=models.CASCADE, verbose_name="Flick")
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE, verbose_name="Platform")
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Price", null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return f"{self.flick.title} on {self.platform.name} - ${self.price}$"
