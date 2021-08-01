from django.contrib import admin
from .models import Doctor, Others, Nurse

# Register your models here.

admin.site.register(Doctor)
admin.site.register(Others)
admin.site.register(Nurse)