from django.urls import path
from . import views

from .views import profile

urlpatterns = [
    path("login/", views.employee_login, name="login"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path('profile/', profile),
    
    path('branches/', views.branch_list, name='branch_list'),
    path('branch/add/', views.add_branch, name='add_branch'),
    path('branch/edit/<int:id>/', views.edit_branch, name='edit_branch'),
    path('branch/delete/<int:id>/', views.delete_branch, name='delete_branch'),
    path('employees/', views.employee_list, name='employee_list'),
path('employee/add/', views.add_employee, name='add_employee'),

path(
    'employee/edit/<int:id>/',
    views.edit_employee,
    name='edit_employee'
),

path(
    'employee/delete/<int:id>/',
    views.delete_employee,
    name='delete_employee'
),

path("logout/", views.user_logout, name="logout"),

]
