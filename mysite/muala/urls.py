from django.urls import path

from . import views

urlpatterns = [
    path('myhtml/', views.index, name='index')
]