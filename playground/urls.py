from django.urls import path
from . import views

# URL_Configuration Module
urlpatterns = [
    path('hello/', views.say_hello)
]
