from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('password_gen/', views.PasswdGenerator, name='passwdgen')
]