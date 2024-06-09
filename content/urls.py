from django.urls import path
from . import views

urlpatterns = [
    path('main/', views.main, name='home'),
    path('o_nas/', views.o_nas, name='o_nas'),
    path('serif/', views.serif, name='serif'),
]
