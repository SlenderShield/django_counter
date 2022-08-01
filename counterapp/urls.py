from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.helloworld),
    path('increment/', views.increment),
    path('decrement/', views.decrement),
    path('reset/', views.reset),

]
