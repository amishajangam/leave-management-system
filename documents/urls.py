from django.urls import path
from . import views

urlpatterns = [

    path(
        '',
        views.documents_page,
        name='documents'
    ),
    
    path(
    'excel/<int:id>/',
    views.view_excel,
    name='view_excel'
),

]