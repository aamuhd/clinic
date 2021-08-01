from django.db import models
from patientsrecords.models import PatientFile
from django.contrib.auth.models import User

# Create your models here.




class RenalFunctionTest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='renals')
    test = models.CharField(max_length=30, default='Renal Funtion Test')
    urea = models.CharField(max_length=30)
    Na = models.CharField(max_length=30)
    HCO3 = models.CharField(max_length=30)
    Cl = models.CharField(max_length=30)
    creatinine = models.CharField(max_length=30)
    

    def __str__(self):
        return self.test

class LiverFunctionTest(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='livers')
    test = models.CharField(max_length=30, default='Liver Funtion Test')
    Alkaline_Phosphate = models.CharField(max_length=30)
    ALT = models.CharField(max_length=30)
    AST = models.CharField(max_length=30)
    Total_Bilirubin = models.CharField(max_length=30)
    Direct_Bilirubin  = models.CharField(max_length=30)
    Total_Protein  = models.CharField(max_length=30)
    Albumin = models.CharField(max_length=30)
    Globulin = models.CharField(max_length=30)
    

    def __str__(self):
        return self.test

class BloodGlucose(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bloods')
    test = models.CharField(max_length=30, default='Blood Glucose')
    Fasting = models.CharField(max_length=30)
    Random = models.CharField(max_length=30)
    two_hours_PP = models.CharField(max_length=30)
    

    def __str__(self):
        return self.user.username