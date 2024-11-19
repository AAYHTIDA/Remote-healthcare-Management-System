

from django.urls import path
from . import views

urlpatterns = [
    path('', views.appointments_list, name='appointments_list'),
    path('<int:id>/', views.appointments_detail, name='appointments_detail'),
    path('create/', views.appointments_create, name='appointments_create'),
    path('<int:id>/edit/', views.appointments_edit, name='appointments_edit'),
]
