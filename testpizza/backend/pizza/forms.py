from django import forms
from .models import Pizza
from django.contrib.auth.models import User


class PizzaForm(forms.ModelForm):
    created_by = forms.ModelChoiceField(queryset=User.objects.all(), widget=forms.HiddenInput())
    class Meta:
        model = Pizza
        fields = ('name', 'toppings', 'description', 'image', 'created_by', 'slug')
