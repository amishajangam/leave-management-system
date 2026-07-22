from django.urls import path

from .views import report_view, export_excel

urlpatterns = [

    path('report/', report_view),

    path('excel/', export_excel),

]