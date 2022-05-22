from django.urls import path, include
from . import views

app_name = "Users"
urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path("sign_up/", views.signup, name="signup"),
    path("logout", views.LogOut, name="logout"),
]