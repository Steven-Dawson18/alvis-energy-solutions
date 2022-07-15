"""
Home urls
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('energy_saving/', views.energy_saving, name="energy_saving"),
    path('how_it_works/', views.how_it_works, name="how_it_works"),
    path('service_life/', views.service_life, name="service_life"),
    path('contact/', views.contact, name="contact"),
]
