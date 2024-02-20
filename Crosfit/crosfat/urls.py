from django.urls import path
from . import views
from django.urls import path
from .views import PlanDetails


app_name = 'crosfat'

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('sign_in/', views.sign_in_view, name='sign_in'),
    path('user/', views.user_view, name='user'),
    path('wyloguj/', views.wyloguj, name='wyloguj'),
    path('create/', views.create, name='create'),
    path('Plans/', views.Plans, name='Plans'),
    path('Edit/', views.edit_user, name='Edit'),
    path('submit_training_plan', views.submit_training_plan, name='submit_training_plan'),
    path('lista_planow/', views.lista_planow, name='lista_planow'),
    path('Plans/<int:pk>/', PlanDetails.as_view(), name='plan_details'),
    path('gen_pl/<int:plan_id>/', views.gen_pl, name='Gen_pl'),
    path('zapisz_cwiczenia/<int:plan_id>/', views.zapisz_cwiczenia_do_planu, name='zapisz_cwiczenia_do_planu'),
]