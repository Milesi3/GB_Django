from django.urls import path
from . import views

urlpatterns = [
    path('main/', views.main_view, name='main'),
    path('about/', views.about_view, name='about'),
]