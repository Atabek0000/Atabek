from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='home'),
    path('o_nas/', views.o_nas, name='o_nas'),
    path('register/', views.register, name='register'),
]
