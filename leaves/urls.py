from django.urls import path
from . import views

from .views import (
    apply_leave,
    approve_leave,
    reject_leave
)

urlpatterns = [

    path('apply/', apply_leave),

    path(
        'approve/<int:id>/',
        approve_leave
    ),

    path(
        'reject/<int:id>/',
        reject_leave
    ),
    
    path(
        'review/<int:id>/',
        views.review_leave,
        name='review_leave'
    ),
    
    path(
    'my-leaves/',
    views.my_leaves,
    name='my_leaves'
),

]