from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_request, name='create_request'),
    path('client/', views.client_page, name='client_page'),
    path('master/', views.master_page, name='master_page'),

    path('accept/<int:request_id>/', views.accept_request, name='accept_request'),

    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
