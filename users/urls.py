from django.urls import path
from . import views

urlpatterns = [
    path("login.html", views.login, name="login"),
]
