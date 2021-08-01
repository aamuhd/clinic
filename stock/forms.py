from django import forms
from .models import *


class MedicineForm(forms.ModelForm):
    

    class Meta:
        model = Medicine
        #fields = ['category', 'name', 'quantity']
        fields = '__all__'
        
        widgets = {
            'name':forms.TextInput(attrs={'class': 'form-control'}),
            'quantity':forms.NumberInput(attrs={'class': 'form-control'}),
        }


class MedicineGivenForm(forms.ModelForm):

    class Meta:
        model = MedicineGiven
        #fields = ['quantity_given',]
        fields = '__all__'

        widgets = {
            'name':forms.TextInput(attrs={'class': 'form-control'}),
            'quantity_given':forms.NumberInput(attrs={'class': 'form-control'}),
        }


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = '__all__'

        widgets = {
            'name':forms.TextInput(attrs={'class': 'form-control'}),
        }
