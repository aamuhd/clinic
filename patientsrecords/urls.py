from django.urls import path
from .import views


app_name = 'patientsrecords'

urlpatterns = [
    path('patientfile/', views.patientfile, name='patientfile'),
    path('patientinfos/', views.patientinfos, name='patientinfos'),
    path('patient_sheet/<int:p_id>/', views.patient_sheet, name='patient_sheet'),
    path('add_sheet/<int:p_id>/', views.add_sheet, name='add_sheet'),
    path('addchart/<int:p_id>/', views.add_chart, name='addchart'),
    path('chart_info/<int:p_id>/', views.chart_info, name='chart_info'),
    path('patient_chart/<int:p_id>/', views.patient_chart, name='patient_chart'),
    path('edit_sheet/<int:p_id>/', views.edit_sheet, name='edit_sheet'),
    path('edit_chart/<int:chart_id>/', views.edit_chart, name='edit_chart'),

    
    
]