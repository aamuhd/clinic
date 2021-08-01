from django.urls import path
from .import views


urlpatterns = [
    path('categories/', views.categories, name='categories'),
    path('medicine/<int:m_id>/', views.medicine, name='medicine'),
    path('add_medicine/<int:m_id>/', views.add_medicine, name='add_medicine'),
    path('category/<int:m_id>/', views.category, name='category'),
    path('view_medicines/', views.view_medicines, name='view_medicines'),
    path('medicine_given/<int:m_id>/', views.medicine_given, name='medicine_given'),
    path('add_category/', views.add_category, name='add_category'),
]