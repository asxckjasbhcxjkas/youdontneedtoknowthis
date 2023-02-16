from django.urls import path, include
from . import views
from django.conf import settings 
from django.conf.urls.static import static


app_name = "Users"
urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path("sign_up/", views.signup, name="signup"),
    path("logout", views.LogOut, name="logout"),
    path('cas_login/', views.cas_login, name='cas_login'),
    path('secure/', views.secure, name='secure'),
    path('cas_logout/', views.cas_logout, name='cas_logout'),
]
