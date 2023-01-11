from django.urls import path
from . import views

urlpatterns = [
    path('insert/', views.insert),
    path('list/', views.listpro),
    path('tomod/',views.csvins)
]