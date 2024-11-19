
from django.urls import path
from . import views

urlpatterns = [
    path('', views.patients_list, name='patients_list'),
    path('<int:id>/', views.patients_detail, name='patients_detail'),
    path('create/', views.patients_create, name='patients_create'),
    path('<int:id>/edit/', views.patients_edit, name='patients_edit'),
]
