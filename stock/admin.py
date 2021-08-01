from django.contrib import admin
from .models import Category, Medicine, MedicineGiven

# Register your models here.
admin.site.register(Category)
admin.site.register(Medicine)
admin.site.register(MedicineGiven)