from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.home,name = 'home'),
    path("register/", views.Register.as_view(), name="register"),
]