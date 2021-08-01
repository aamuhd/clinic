from django import forms
from .models import PatientFile, ClientSheet, ObservationChart
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Row, Column
from crispy_forms.bootstrap import FormActions




class PatientForm(forms.ModelForm):

    class Meta:
        model = PatientFile

        fields = [
            'image',
            'firstname', 'surname', 'lastname', 'department', 'phone',
            'date_of_birth', 'next_of_kin', 'relationship', 'address_of_next_of_kin',
            'phone_of_next_of_kin', 'place_of_origin', 'tribe', 'religion',
            'occupation', 
        ]
       
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        #self.helper.add_input(Submit('save', 'Save', css_class='btn btn-secondary'))

        self.helper.layout = Layout(
            Row(
                Column('image', css_class='col-md-2')
            ),
            Row(
               Column('lastname'),
               Column('surname'),
               Column('firstname')   
            ),
            Row(
                
                Column('date_of_birth'),
                Column('department'),
                Column('phone')
            ),
            Row(
                
                Column('next_of_kin'),
                Column('relationship'),
                Column('occupation')
            ),
            
            Row(
                
                Column('phone_of_next_of_kin'),
                Column('place_of_origin'),
                Column('religion')
            ),
            Row(
                Column('address_of_next_of_kin', rows="3")
            ),
            FormActions(
                Submit('save', 'Save', css_class='btn btn-secondary')
            )
        )
        

"""

        widgets = {
            
            
            'address_of_next_of_kin': forms.Textarea(attrs={'class': 'col-md-4'}),
            'firstname': forms.TextInput(attrs={'class': 'col-md-4'}),
            'surname': forms.TextInput(attrs={'class': 'col-md-4'}),
            'lastname': forms.TextInput(attrs={'class': 'col-md-4'}),
            'department': forms.TextInput(attrs={'class': 'col-md-4'}),
            'phone': forms.TextInput(attrs={'class': 'col-md-4'}),
            'date_of_birth': forms.TextInput(attrs={'class': 'col-md-4'}),
            'next_of_kin': forms.TextInput(attrs={'class': 'col-md-4'}),
            'relationship': forms.TextInput(attrs={'class': 'col-md-4'}),
            'address_of_next_of_kin': forms.TextInput(attrs={'class': 'col-md-4'}),
            'phone_of_next_of_kin': forms.TextInput(attrs={'class': 'col-md-4'}),
            'place_of_origin': forms.TextInput(attrs={'class': 'col-md-4'}),
            'tribe': forms.TextInput(attrs={'class': 'col-md-4'}),
            'religion': forms.TextInput(attrs={'class': 'col-md-4'}),
            'occupation': forms.TextInput(attrs={'class': 'col-md-4'}),
            
            }

"""

class SheetForm(forms.ModelForm):

    class Meta:
        model = ClientSheet
        fields = [
            'text', 'department', 'name', 'age', 'sex', 'marital_status',
            'occupation', 
        ]
        
        labels = {'text': ''}
    
   

        
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Enter priscription here'}),
            'department': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.TextInput(attrs={'class': 'form-control'}),
            'sex': forms.Select(attrs={'class': 'form-control'}),
            'marital_status': forms.TextInput(attrs={'class': 'form-control'}),
            'occupation': forms.TextInput(attrs={'class': 'form-control'}),
        
        }

        

class ChartForm(forms.ModelForm):

    class Meta:
        model = ObservationChart
        fields = [
            'surname', 'firstname', 'age', 'card_no', 'BP', 'temperature', 'pulse',
            'respiration', 
        ]
        
        #labels = {'text': ''}
    
        

        widgets = {
            'surname': forms.TextInput(attrs={'class':'form-control'}),
            'firstname': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.TextInput(attrs={'class': 'form-control'}),
            'card_no': forms.TextInput(attrs={'class': 'form-control'}),
            'BP': forms.TextInput(attrs={'class': 'form-control'}),
            'temperature': forms.TextInput(attrs={'class': 'form-control'}),
            'pulse': forms.TextInput(attrs={'class': 'form-control'}),
            'respiration': forms.TextInput(attrs={'class': 'form-control'}),
            'medication': forms.TextInput(attrs={'class': 'form-control'}),
            
        
        }

    

    
   
  
    