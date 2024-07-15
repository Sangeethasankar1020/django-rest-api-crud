from django.contrib import admin
from django.urls import path,include
from Employeeapp import views


urlpatterns = [
    path('department/', views.departmentApiList, name='department_list'),  # Endpoint for listing and adding departments
    path('department/<int:pk>/', views.departmentApiDetail, name='department_detail'),  # Endpoint for retrieving, updating, and deleting departments by ID
]