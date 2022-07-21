"""
Products urls
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.products, name="products"),
    path('ecoflo_smart/', views.ecoflo_smart, name="ecoflo_smart"),
]
