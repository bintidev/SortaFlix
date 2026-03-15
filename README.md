# SortaFlix — Tu mini cine personal 🎞️✨

SortaFlix es una app sencilla hecha en Django para guardar tus películas, las plataformas donde las ves y el precio si aplica. Ideal para organizar tu colección y saber dónde ver cada título.

<p align="center">🏴󠁧󠁢󠁥󠁮󠁧󠁿 <a href="README.md">README English version</a></p>

## 🧩 Features

- 🎬 Añadir y organizar películas (portada, título, director, año, géneros, duración, puntuación, estado).
- 📺 Registrar y listar plataformas (logo, tipo, áreas, descripción).
- 🔗 Vincular películas con plataformas y anotar precios.
- 🔐 Registro e inicio de sesión; cada usuario gestiona sus propios registros.

## ⚙️ Instalación y configuración

1. Crea y activa un entorno virtual

```powershell
python -m venv .venv
.\\.venv\\Scripts\\Activate.ps1
```

2. Instala dependencias mínimas

```powershell
pip install django==6.0.1 Pillow
```

3. Aplica migraciones (crea la base de datos)

```powershell
python manage.py migrate
```

4. (Opcional) Crea un superusuario

```powershell
python manage.py createsuperuser
```

5. (Opcional y con cuidado) Poblar datos de ejemplo

```powershell
python manage.py seed
```

Nota: el comando `seed` borra usuarios y datos existentes — úsalo sólo en entornos de prueba.

6. Levanta el servidor

```powershell
python manage.py runserver
```

Abre http://127.0.0.1:8000/ en tu navegador.

> 🔔 NOTA IMPORTANTE
>
> - `media/` está ignorado por Git: las portadas y logos no se suben. Si usas `seed` puede que falten imágenes. Opciones:
>   - Añadir imágenes de ejemplo versionadas en `media/`, creada manualmente en la raíz del proyecto.
>   - Editar `seed.py` para usar placeholders (URLs o texto) en vez de ficheros locales.
> - `db.sqlite3` está en `.gitignore`: en un clon limpio ejecuta `python manage.py migrate` antes de usar la app.
> - `sort_a_flix/settings.py` incluye una `SECRET_KEY` y `DEBUG = True`. Para producción mueve la clave a una variable de entorno y pon `DEBUG = False`.

## 📸 Capturas

![Landing — Home page](pictures/home-page.png)

Landing — Pantalla inicial

![Dashboard](pictures/dashboard.png)

Dashboard — Resumen del usuario

![Colección — Flixs](pictures/flixs.png)

Flixs — Lista de películas

![Detalle de película](pictures/flix-detail.png)

Flix detail — Información de la película

![Editar película](pictures/flix-update.png)

Edit flix — Formulario de edición

![Plataformas](pictures/platforms.png)

Platforms — Lista de plataformas

![Detalle plataforma](pictures/platform-detail.png)

Platform detail — Información de la plataforma

![Disponibilidades](pictures/availabilities.png)

Availabilities — Precios y disponibilidad

![Modal de borrado](pictures/delete-modal.png)

Delete modal — Confirmación de borrado

---

<p align='center'>
Made with ❤ by bintidev · SortaFlix
</p>
