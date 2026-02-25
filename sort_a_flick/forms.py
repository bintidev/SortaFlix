from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from saf_start.models import Flick, Platform, Availability
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

FIELD_CLASS = 'w-full px-4 py-3 bg-[#0F0F1E] border border-gray-700 rounded-lg text-white placeholder-gray-500 focus:border-[#6C63FF] focus:ring-2 focus:ring-[#6C63FF] focus:outline-none'

class SignupForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

        widgets = {
            'username': forms.TextInput(attrs={
                'class': FIELD_CLASS,
                'placeholder': 'Username'
            })
        }

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(attrs={
            'class': FIELD_CLASS,
            'placeholder': 'Password'
        })
        self.fields['password2'].widget = forms.PasswordInput(attrs={
            'class': FIELD_CLASS,
            'placeholder': 'Confirm password'
        })

class SigninForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.fields['username'].widget = forms.TextInput(attrs={
            'class': FIELD_CLASS,
            'placeholder': 'Username'
        })
        self.fields['password'].widget = forms.PasswordInput(attrs={
            'class': FIELD_CLASS,
            'placeholder': 'Password'
        })
    


# formulario basado en el modelo Flicks
class FlickForm(ModelForm):
    class Meta:
        model = Flick
        fields = ['cover_image', 'title', 'director', 'year', 'genres', 'rating', 'duration', 'synopsis', 'status']

        # estilos de campos personalizados
        widgets = {
            'title': forms.TextInput(attrs={
                'class': FIELD_CLASS,
                'placeholder': 'Movie title'
            }),

            'director': forms.TextInput(attrs={
                'class': FIELD_CLASS,
                'placeholder': 'Director name'
            }),

            'year': forms.NumberInput(attrs={
                'class': FIELD_CLASS,
                'placeholder': 'Year of release'
            }),
            
            'description': forms.Textarea(attrs={
                'class': FIELD_CLASS,
                'rows': 4,
                'placeholder': 'Movie description'
            }),

            'genres': forms.CheckboxSelectMultiple(attrs={
                'class': 'text-black focus:ring-[#6C63FF]'
            }),

            'rating': forms.NumberInput(attrs={
                'class': FIELD_CLASS,
                'placeholder': 'Rating (0-5)',
                'step': 0.1,
                'min': 0,
                'max': 10
            }),

            'duration': forms.NumberInput(attrs={
                'class': FIELD_CLASS,
                'placeholder': 'In minutes'
            }),
                        
            'synopsis': forms.Textarea(attrs={
                'class': FIELD_CLASS,
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
                'class': FIELD_CLASS,
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
                'class': FIELD_CLASS,
                'placeholder': 'Parent company (optional)'
            }),

            'areas_served': forms.TextInput(attrs={
                'class': FIELD_CLASS,
                'placeholder': 'Areas served (optional)'
            }),

            'url': forms.TextInput(attrs={
                'class': FIELD_CLASS,
                'placeholder': 'URL'
            }),

            'description': forms.Textarea(attrs={
                'class': FIELD_CLASS,
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
                'class': FIELD_CLASS,
                'placeholder': 'Price (optional)',
                'step': 0.01,
                'min': 0
            }),

        }