from django import forms
from django.forms import ModelForm
from raf_start.models import Flick, Platform, Availability, Genre

# formulario basado en el modelo Flicks
class FlickForm(ModelForm):
    class Meta:
        model = Flick
        fields = ['cover_image', 'title', 'director', 'year', 'genre', 'rating', 'synopsis', 'status']

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

            'genre': forms.CheckboxSelectMultiple(attrs={
                'class': 'text-black focus:ring-[#6C63FF]'
            }),

            'rating': forms.NumberInput(attrs={
                'class': 'w-full px-4 py-3 bg-[#0F0F1E] border border-gray-700 rounded-lg text-white placeholder-gray-500 focus:border-[#6C63FF] focus:ring-2 focus:ring-[#6C63FF] focus:outline-none',
                'placeholder': 'Rating (0-5)',
                'step': 0.1,
                'min': 0,
                'max': 5
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

        }

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