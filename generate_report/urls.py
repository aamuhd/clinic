from django.urls import path
from .import views


urlpatterns = [
    path('report/', views.view_report, name='report'),
    path('report_pdf/<int:my_id>/', views.download_report, name='report_pdf'),
    path('glucose/', views.bloodGlucoseTest, name='glucose'),
    path('renal/', views.renalTest, name='renal'),
    path('liver/', views.liverTest, name='liver'),
    path('search-file/', views.patientFilterView, name='search-file'),
    path('records/<int:p_id>/', views.record, name='records'),
    path('edit/<int:mc>/', views.edit_test, name='edit'),
]