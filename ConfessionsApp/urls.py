from django.urls import path 
from . import views

app_name = "ConfessionsApp"
urlpatterns = [
    path("", views.index, name="index"),
    path("base/", views.base, name="base"),
    path("questions", views.questions, name="questions"),
    path("question/<int:q_id>/", views.question, name="question"),
    path("confessions/", views.confessions, name="confessions"),
    path("likeconfession/<int:c_id>", views.likeconfession, name="likeconfession"),
    path("privacy-policy/", views.privacy, name="privacy"),
    path("about/", views.about, name="about"),
]
