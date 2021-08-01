from django.urls import path
from .views import (
    HomeView,
    MainPageDetailView,
    contactView,
    user_profile,
    edit_profile,
)
from . import views

app_name = 'core'
urlpatterns = [
    path('p/<str:slug>/', MainPageDetailView.as_view(), name='page'),
    path('contact/', contactView, name='contact'),
    path('', HomeView.as_view(), name='home'),
    path('user/<str:slug_id>/', views.user_profile, name="user"),
    path('edit-profile/<str:slug_id>/', views.edit_profile, name="edit_profile"),
    path('p/appointment', views.appointment, name='appointment'),
    
]
