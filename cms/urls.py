from django.urls import path
from . import views

urlpatterns = [

    path(
        'cms/',
        views.notice_list,
        name='notice_list'
    ),

    path(
        'cms/add/',
        views.add_notice,
        name='add_notice'
    ),

path(
    'cms/edit/<int:id>/',
    views.edit_notice,
    name='edit_notice'
),

path(
    'cms/delete/<int:id>/',
    views.delete_notice,
    name='delete_notice'
)
]