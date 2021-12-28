from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home_page"),
    path('first/', views.first, name="first_page"),
    path('second/<str:pk>/', views.second, name='second_page'),
    path('third/', views.third, name="third_page"),
]
