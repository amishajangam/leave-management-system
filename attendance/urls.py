from django.urls import path
from . import views

urlpatterns = [

    # Attendance Report
    path(
        'attendance/',
        views.attendance_report,
        name='attendance_report'
    ),

    # Attendance List
    path(
        'attendance/list/',
        views.attendance_list,
        name='attendance_list'
    ),

    # Add Attendance
    path(
        'attendance/add/',
        views.add_attendance,
        name='add_attendance'
    ),
    
    path(
    'attendance/edit/<int:id>/',
    views.edit_attendance,
    name='edit_attendance'
),

path(
    'attendance/delete/<int:id>/',
    views.delete_attendance,
    name='delete_attendance'
),

]