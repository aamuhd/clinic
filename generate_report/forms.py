from .models import BloodGlucose, RenalFunctionTest, LiverFunctionTest
from django import forms


class BloodGlucoseForm(forms.ModelForm):

    class Meta:
        model = BloodGlucose
        fields = '__all__'

        widgets = {
            'user': forms.TextInput(attrs={'class': 'form-control'}),
            'test': forms.TextInput(attrs={'class': 'form-control'}),
            'Fasting': forms.TextInput(attrs={'class': 'form-control'}),
            'Random': forms.TextInput(attrs={'class': 'form-control'}),
            'two_hours_PP': forms.TextInput(attrs={'class': 'form-control'}),
        }

class RenalFunctionTestForm(forms.ModelForm):
    
    class Meta:
        model = RenalFunctionTest
        fields = '__all__'

        widgets = {
            'user': forms.Select(attrs={'class':'form-control'}),
            'test': forms.TextInput(attrs={'class':'form-control'}),
            'urea': forms.TextInput(attrs={'class':'form-control'}),
            'Na': forms.TextInput(attrs={'class':'form-control'}),
            'HCO3': forms.TextInput(attrs={'class':'form-control'}),
            'Cl': forms.TextInput(attrs={'class':'form-control'}),
            'creatinine': forms.TextInput(attrs={'class':'form-control'}),
        }
    

class LiverFunctionTestForm(forms.ModelForm):
    
    class Meta:
        model = LiverFunctionTest
        fields = '__all__'

        widgets = {
            'user': forms.Select(attrs={'class':'form-control'}),
            'test': forms.TextInput(attrs={'class':'form-control'}),
            'Alkaline_Phosphate': forms.TextInput(attrs={'class':'form-control'}),
            'ALT': forms.TextInput(attrs={'class':'form-control'}),
            'AST': forms.TextInput(attrs={'class':'form-control'}),
            'Total_Bilirubin': forms.TextInput(attrs={'class':'form-control'}),
            'Direct_Bilirubin': forms.TextInput(attrs={'class':'form-control'}),
            'Total_Protein': forms.Select(attrs={'class':'form-control'}),
            'Albumin': forms.Select(attrs={'class':'form-control'}),
            'Globulin': forms.Select(attrs={'class':'form-control'}),
        }