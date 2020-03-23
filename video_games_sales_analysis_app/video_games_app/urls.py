from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.add_data,name='add-data'),
    path('pie-chart/', views.pie_chart, name='pie-chart'),
    path('add-data/',views.add_data,name='add-data'),
]
