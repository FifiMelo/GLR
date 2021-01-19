from django.urls import path
from . import views

urlpatterns = [
    path('send/', views.v1),
    path('thanks/', views.v2)
]