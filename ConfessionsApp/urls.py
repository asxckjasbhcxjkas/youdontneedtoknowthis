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
    path("deleteconfession/<int:c_id>", views.deleteconfession, name="deleteconfession"),
    path("editconfessions/<int:c_id>", views.editconfession, name="editconfession"),
    path("myconfessions", views.userConfessions, name="myconfessions"),
    path("myquestions", views.userQuestions, name="myquestions"),
    path("mycomments", views.userComments, name="mycomments"),
    path("privacy-policy/", views.privacy, name="privacy"),
    path("about/", views.about, name="about"),

]
