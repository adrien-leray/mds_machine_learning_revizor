from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index,name='index'),
    path('pie-chart/', views.pie_chart, name='pie-chart'),
]
