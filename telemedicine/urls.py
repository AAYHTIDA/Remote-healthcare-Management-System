from django.urls import path
from . import views

urlpatterns = [
    path('', views.telemedicine_list, name='telemedicine_list'),
    path('<int:id>/', views.telemedicine_detail, name='telemedicine_detail'),
    path('create/', views.telemedicine_create, name='telemedicine_create'),
    path('<int:id>/edit/', views.telemedicine_edit, name='telemedicine_edit'),
]
