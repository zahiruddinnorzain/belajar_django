from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('borang/', views.get_name, name='blog-get_name'),
    path('contact/', views.get_contact, name='blog-get_contact'),
]
