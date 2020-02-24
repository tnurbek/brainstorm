from django.urls import path
from . import views

urlpatterns =[
    path('signUp', views.SignUp, name='register'),
    path('signIn', views.SignIn, name='login')
]