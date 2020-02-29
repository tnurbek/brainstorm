from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.create_group, name='create_group'),
    path('in', views.initial, name='initial'),
    path('validation/<int:pk>', views.validate_group, name='validation')
]