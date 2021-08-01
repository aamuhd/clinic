from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.contrib.auth.models import User

# Create your models here.

class PatientFile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images', blank=True, null=True)
    #slug_id = models.SlugField(blank=True, null=True)
    firstname = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    department = models.CharField(max_length=90)
    phone = models.CharField(max_length=20)
    date_of_birth = models.DateField(help_text='yy-mm-dd')
    next_of_kin = models.CharField(max_length=50)
    relationship = models.CharField(max_length=50)
    address_of_next_of_kin = models.TextField()
    phone_of_next_of_kin = models.CharField(max_length=20)
    place_of_origin = models.CharField(max_length=30)
    tribe = models.CharField(max_length=30, blank=True, null=True)
    religion = models.CharField(max_length=30)
    occupation = models.CharField(max_length=50)


    class Meta:
        verbose_name = 'Patient File'
        verbose_name_plural = 'Patients File'


    def __str__(self):
        return self.firstname




class ClientSheet(models.Model):

    Gender = (('Male', 'male'), ('female', 'female'))
    
    patientfile = models.ForeignKey(PatientFile, on_delete=models.CASCADE)
    department = models.CharField(max_length=50, default='student')
    name = models.CharField(max_length=90)
    age = models.CharField(max_length=10)
    sex = models.CharField(max_length=10, choices=Gender)
    marital_status = models.CharField(max_length=10)
    occupation = models.CharField(max_length=20, default='student')
    reg_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    text = models.TextField() 


    def __str__(self):
        return self.name 
    

class ObservationChart(models.Model):

    
    
    patientfile = models.ForeignKey(PatientFile, on_delete=models.CASCADE)
    surname = models.CharField(max_length=50, default='student')
    firstname = models.CharField(max_length=90)
    age = models.CharField(max_length=10, default='20')
    card_no = models.CharField(max_length=15)

    BP = models.CharField(max_length=20, default='student')
    temperature = models.CharField(max_length=10)
    pulse = models.CharField(max_length=15)
    respiration = models.CharField(max_length=15)
    medication = models.TextField()
    reg_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    