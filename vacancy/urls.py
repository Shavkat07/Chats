from django.urls import path
from . import views


urlpatterns = [
    path('all', views.vacancy_list, name='vacancy_list'),
    path('<int:vacancy_id>/', views.vacancy_detail, name='vacancy_detail'),
    path('create/', views.create_vacancy, name='create_vacancy'),
]