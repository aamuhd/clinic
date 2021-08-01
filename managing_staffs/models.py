from django.db import models
from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save


# Create your models here.

class Doctor(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=80)
    department = models.CharField(max_length=90)
    position = models.CharField(max_length=30)
    email = models.EmailField(null=True)
    

    def __str__(self):
        return self.fullname


class Others(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=80)
    position = models.CharField(max_length=30)
    email = models.EmailField(null=True)

    class Meta:
        verbose_name_plural = 'Others'

    def __str__(self):
        return self.fullname

class Nurse(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=80)
    department = models.CharField(max_length=90)
    email = models.EmailField(null=True)
    
    
    def __str__(self):
        return self.fullname


"""
def create_doctor_profile(sender, instance, created, *args, **kwargs):
    if created:

        group = Group.objects.get(name='others')
        instance.groups.add(group)
        others = Others.objects.create(
                    user = instance,
                    #email = instance.email,
                    fullname = instance.username
                )
            

post_save.connect(create_doctor_profile, sender=User)
"""