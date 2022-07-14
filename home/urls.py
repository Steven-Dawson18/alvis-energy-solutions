"""
Home urls
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('energy_saving/', views.energySaving, name="energy_saving"),
    path('contact/', views.contact, name="contact"),
]
