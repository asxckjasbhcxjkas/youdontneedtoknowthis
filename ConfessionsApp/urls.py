from django.urls import path 
from . import views

app_name = "ConfessionsApp"
urlpatterns = [

    path("", views.index, name="index"),

    path("questions", views.questions, name="questions"),
    path("question/<int:q_id>/", views.question, name="question"),
    path("editquestion/<int:q_id>/", views.editquestion, name="editquestion"),
    path("deletequestion/<int:q_id>/", views.deletequestion, name="deletequestion"),

    path("confessions/", views.confessions, name="confessions"),
    path("deleteconfession/<int:c_id>", views.deleteconfession, name="deleteconfession"),
    path("editconfessions/<int:c_id>", views.editconfession, name="editconfession"),

    path("deletecomment/<int:q_id>/<int:cm_id>", views.deletecomment, name="deletecomment"),
    path("editcomment/<int:q_id>/<int:cm_id>/", views.editcomment, name="editcomment"),
    path("myconfessions", views.userConfessions, name="myconfessions"),
    path("myquestions", views.userQuestions, name="myquestions"),
    path("mycomments", views.userComments, name="mycomments"),
]
