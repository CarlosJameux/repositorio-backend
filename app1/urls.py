from django.urls import path
from . import views

urlpatterns = [
    path('v1/', views.vista1, name='vista1'),
]