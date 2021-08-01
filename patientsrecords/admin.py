from django.contrib import admin
from .models import PatientFile, ClientSheet, ObservationChart


# Register your models here.


admin.site.register(ClientSheet)
admin.site.register(ObservationChart)
admin.site.register(PatientFile)


"""
class SheetInline(admin.TabularInline):
    
    model = ClientSheet
    extra = 0
    readonly_fields = ["reg_date","updated"]

class ChartInline(admin.TabularInline):
    
    model = ObservationChart
    extra = 0
    readonly_fields = ["reg_date","updated"]

class SheetAdmin(admin.ModelAdmin):
    
    inlines = [SheetInline, ChartInline]
    
    class Meta:
        model = PatientFile
        

admin.site.register(PatientFile, SheetAdmin)
"""