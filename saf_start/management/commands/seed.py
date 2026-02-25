from django.core.management.base import BaseCommand
from saf_start.models import Flick, Genre
from django.contrib.auth.models import User
from django.db import connection

# datos de inicializacion de la base de datos
class Command(BaseCommand):
    help = 'Llena la base de datos con películas de ejemplo'

    def handle(self, *args, **options):
        # Borrar datos anteriores
        print("🗑️  Clearing old data...")

        with connection.cursor() as cursor:
            cursor.execute('PRAGMA foreign_keys = OFF;')

        # limpia las relaciones
        for flick in Flick.objects.all():
            flick.genres.clear()

        Flick.objects.all().delete()
        Genre.objects.all().delete()
        User.objects.all().delete()  # Borra TODOS
        
        print("🎬 Creating fake flicks and users...")
        
        # crear géneros de pelicula
        # se almacenan los objetos en variables para luego hacer referencia a ellos
        # en el modelo Flick (ManyToMany)
        action = Genre.objects.create(name='Action')
        comedy = Genre.objects.create(name='Comedy')
        fantasy = Genre.objects.create(name='Fantasy')
        thriller = Genre.objects.create(name='Thriller')
        horror = Genre.objects.create(name='Horror')
        scifi = Genre.objects.create(name='Science Fiction')
        romance = Genre.objects.create(name='Romance')
        drama = Genre.objects.create(name='Drama')
        documental = Genre.objects.create(name='Documental')
        animation = Genre.objects.create(name='Animation')
        supernatural = Genre.objects.create(name='Supernatural')

        # crear usuarios
        iluvflicks = User.objects.create(username='iluvflicks')
        iluvflicks.set_password('1a2b3c')
        iluvflicks.save()


        sharperdanaknife = User.objects.create(username='sharperdanaknife')
        sharperdanaknife.set_password('!tsaKnifee')
        sharperdanaknife.save()

        
        whosiwolvie = User.objects.create(username='whoiswolvie')
        whosiwolvie.set_password('bubwudah3lly')
        whosiwolvie.save()

        
        # crear películas
        sharper = Flick.objects.create(
            cover_image='covers/sharper.jpg',
            user=User.objects.get(username='sharperdanaknife'),
            title='Sharper',
            director='Benjamin Caron',
            year=2010,
            rating=6.1,
            duration=117,
            synopsis='No one is what they seem in this neo-noir thriller set in New York, where relentless manipulation and dangerous power games reign supreme.',
            status='Watched'
        )

        sharper.genres.add(thriller)

        wolverine = Flick.objects.create(
            cover_image='covers/wolverine.jpg',
            user=User.objects.get(username='whoiswolvie'),
            title='The Wolverine',
            director='James Mangold',
            year=2013,
            rating=6.7,
            duration=137,
            synopsis='Wolverine comes to Japan to meet an old friend whose life he saved years ago, and gets embroiled in a conspiracy involving yakuza and mutants.',
            status='Watch'
        )

        wolverine.genres.add(thriller, scifi)

        fnaf = Flick.objects.create(
            cover_image='covers/fnaf.jpg',
            user=User.objects.get(username='iluvflicks'),
            title='Five Nights at Freddy\'s',
            director='Emma Tammi',
            year=2023,
            rating=5.4,
            duration=110,
            synopsis='A troubled security guard begins working at Freddy Fazbear\'s Pizza. As he spends his first night on the job, he realizes that the night shift at Freddy\'s won\'t be so easy to get through.',
            status='Watch'
        )

        fnaf.genres.add(horror, supernatural, thriller)
        
        print("✅ ¡Listo!")