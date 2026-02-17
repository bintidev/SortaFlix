from django import forms
from django.forms import ModelForm
from saf_start.models import Flick, Platform, Availability
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class UserCreationForm():
    class Meta:
        fields = ['username', 'password']

        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 bg-[#0F0F1E] border border-gray-700 rounded-lg text-white placeholder-gray-500 focus:border-[#6C63FF] focus:ring-2 focus:ring-[#6C63FF] focus:outline-none',
                'placeholder': 'Username'
            }),

            'password': forms.PasswordInput(attrs={
                'class': 'w-full px-4 py-3 bg-[#0F0F1E] border border-gray-700 rounded-lg text-white placeholder-gray-500 focus:border-[#6C63FF] focus:ring-2 focus:ring-[#6C63FF] focus:outline-none',
                'placeholder': 'Password'
            }),
        }

class AuthenticationForm():
    class Meta:
        fields = ['username', 'password1', 'password2']

        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 bg-[#0F0F1E] border border-gray-700 rounded-lg text-white placeholder-gray-500 focus:border-[#6C63FF] focus:ring-2 focus:ring-[#6C63FF] focus:outline-none',
                'placeholder': 'Username'
            }),

            'password1': forms.PasswordInput(attrs={
                'class': 'w-full px-4 py-3 bg-[#0F0F1E] border border-gray-700 rounded-lg text-white placeholder-gray-500 focus:border-[#6C63FF] focus:ring-2 focus:ring-[#6C63FF] focus:outline-none',
                'placeholder': 'Password'
            }),

            'password2': forms.PasswordInput(attrs={
                'class': 'w-full px-4 py-3 bg-[#0F0F1E] border border-gray-700 rounded-lg text-white placeholder-gray-500 focus:border-[#6C63FF] focus:ring-2 focus:ring-[#6C63FF] focus:outline-none',
                'placeholder': 'Password'
            })
        }
    


# formulario basado en el modelo Flicks
class FlickForm(ModelForm):
    class Meta:
        model = Flick
        fields = ['cover_image', 'title', 'director', 'year', 'genres', 'rating', 'synopsis', 'status']

        # estilos de campos personalizados
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 bg-[#0F0F1E] border border-gray-700 rounded-lg text-white placeholder-gray-500 focus:border-[#6C63FF] focus:ring-2 focus:ring-[#6C63FF] focus:outline-none',
                'placeholder': 'Movie title'
            }),

            'director': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 bg-[#0F0F1E] border border-gray-700 rounded-lg text-white placeholder-gray-500 focus:border-[#6C63FF] focus:ring-2 focus:ring-[#6C63FF] focus:outline-none',
                'placeholder': 'Director name'
            }),

            'year': forms.NumberInput(attrs={
                'class': 'w-full px-4 py-3 bg-[#0F0F1E] border border-gray-700 rounded-lg text-white placeholder-gray-500 focus:border-[#6C63FF] focus:ring-2 focus:ring-[#6C63FF] focus:outline-none',
                'placeholder': 'Year of release'
            }),
            
            'description': forms.Textarea(attrs={
                'class': 'w-full px-4 py-3 bg-[#0F0F1E] border border-gray-700 rounded-lg text-white placeholder-gray-500 focus:border-[#6C63FF] focus:ring-2 focus:ring-[#6C63FF] focus:outline-none resize-none',
                'rows': 4,
                'placeholder': 'Movie description'
            }),

            'genres': forms.CheckboxSelectMultiple(attrs={
                'class': 'text-black focus:ring-[#6C63FF]'
            }),

            'rating': forms.NumberInput(attrs={
                'class': 'w-full px-4 py-3 bg-[#0F0F1E] border border-gray-700 rounded-lg text-white placeholder-gray-500 focus:border-[#6C63FF] focus:ring-2 focus:ring-[#6C63FF] focus:outline-none',
                'placeholder': 'Rating (0-5)',
                'step': 0.1,
                'min': 0,
                'max': 10
            }),
                        
            'synopsis': forms.Textarea(attrs={
                'class': 'w-full px-4 py-3 bg-[#0F0F1E] border border-gray-700 rounded-lg text-white placeholder-gray-500 focus:border-[#6C63FF] focus:ring-2 focus:ring-[#6C63FF] focus:outline-none resize-none',
                'rows': 4,
                'placeholder': 'Movie synopsis'
            }),

            'status': forms.Select(attrs={
                'class': 'w-full px-4 py-3 bg-[#0F0F1E] border border-gray-700 rounded-lg text-white focus:border-[#6C63FF] focus:ring-2 focus:ring-[#6C63FF] focus:outline-none'
            }),
            
            'cover_image': forms.FileInput(attrs={
                'class': 'w-full text-white file:mr-4 file:py-2 file:px-4 file:rounded-lg file:border-0 file:bg-gradient-to-r file:from-[#6C63FF] file:to-[#4ECDC4] file:text-white file:cursor-pointer hover:file:opacity-90',
                'accept': 'image/*'
            }),
        }

# formulario basado en el modelo Flicks
class PlatformForm(ModelForm):
    class Meta:
        model = Platform
        fields = ['name', 'delivery_type']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 bg-[#0F0F1E] border border-gray-700 rounded-lg text-white placeholder-gray-500 focus:border-[#6C63FF] focus:ring-2 focus:ring-[#6C63FF] focus:outline-none',
                'placeholder': 'Platform name'
            }),

            'delivery_type': forms.Select(attrs={
                'class': 'w-full px-4 py-3 bg-[#0F0F1E] border border-gray-700 rounded-lg text-white focus:border-[#6C63FF] focus:ring-2 focus:ring-[#6C63FF] focus:outline-none'
            }),

            'logo': forms.FileInput(attrs={
                'class': 'w-full text-white file:mr-4 file:py-2 file:px-4 file:rounded-lg file:border-0 file:bg-gradient-to-r file:from-[#6C63FF] file:to-[#4ECDC4] file:text-white file:cursor-pointer hover:file:opacity-90',
                'accept': 'image/*'
            }),

            'parent': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 bg-[#0F0F1E] border border-gray-700 rounded-lg text-white placeholder-gray-500 focus:border-[#6C63FF] focus:ring-2 focus:ring-[#6C63FF] focus:outline-none',
                'placeholder': 'Parent company (optional)'
            }),

            'areas_served': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 bg-[#0F0F1E] border border-gray-700 rounded-lg text-white placeholder-gray-500 focus:border-[#6C63FF] focus:ring-2 focus:ring-[#6C63FF] focus:outline-none',
                'placeholder': 'Areas served (optional)'
            }),

            'url': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 bg-[#0F0F1E] border border-gray-700 rounded-lg text-white placeholder-gray-500 focus:border-[#6C63FF] focus:ring-2 focus:ring-[#6C63FF] focus:outline-none',
                'placeholder': 'URL'
            }),

            'description': forms.Textarea(attrs={
                'class': 'w-full px-4 py-3 bg-[#0F0F1E] border border-gray-700 rounded-lg text-white placeholder-gray-500 focus:border-[#6C63FF] focus:ring-2 focus:ring-[#6C63FF] focus:outline-none resize-none',
                'rows': 4,
                'placeholder': 'Platform description'
            }),
        }

# formulario basado en el modelo Flicks
class AvailabilityForm(ModelForm):
    class Meta:
        model = Availability
        fields = ['flick', 'platform', 'price']

        widgets = {
            'flick': forms.Select(attrs={
                'class': 'w-full px-4 py-3 bg-[#0F0F1E] border border-gray-700 rounded-lg text-white focus:border-[#6C63FF] focus:ring-2 focus:ring-[#6C63FF] focus:outline-none'
            }),

            'platform': forms.Select(attrs={
                'class': 'w-full px-4 py-3 bg-[#0F0F1E] border border-gray-700 rounded-lg text-white focus:border-[#6C63FF] focus:ring-2 focus:ring-[#6C63FF] focus:outline-none'
            }),

            'price': forms.NumberInput(attrs={
                'class': 'w-full px-4 py-3 bg-[#0F0F1E] border border-gray-700 rounded-lg text-white placeholder-gray-500 focus:border-[#6C63FF] focus:ring-2 focus:ring-[#6C63FF] focus:outline-none',
                'placeholder': 'Price (optional)',
                'step': 0.01,
                'min': 0
            }),

        }