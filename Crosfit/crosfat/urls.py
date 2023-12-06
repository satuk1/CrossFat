from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('sign_in/', views.sign_in_view, name='sign_in'),
    path('user/', views.user_view, name='user'),
    path('wyloguj/', views.wyloguj, name='wyloguj'),
    path('Utworz', views.Utworz, name='Utworz plan'),
]