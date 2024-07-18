from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.home,name = 'home'),                          #Home page
    path("register/", views.Register.as_view(), name="register"),#To registration
]