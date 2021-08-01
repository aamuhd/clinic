from django.contrib import admin
from .models import LiverFunctionTest, RenalFunctionTest, BloodGlucose


admin.site.register(LiverFunctionTest)
admin.site.register(RenalFunctionTest)
admin.site.register(BloodGlucose)

# Register your models here.
