from django.shortcuts import render, redirect
from .models import Question, Post, PostComment, Like, Confession
from django.db.models import Count
# Create your views here.

def index(request):
    return render(request, "ConfessionsApp/index.html")

def base(request):
    return render(request, "ConfessionsApp/base.html")

def questions(request):
    if request.method != "POST":
        Questions = Question.objects.all()
        print(Questions[0].num_days_ago)

        context = {
            "Questions": Questions,
        }

        return render(request, "ConfessionsApp/questions.html", context)

    else:
        question = Question.objects.create(question_text=request.POST["QuestionInput"], owner=request.user)
        Questions = Question.objects.all()
        print(Questions[0].num_days_ago)

        context = {
            "Questions": Questions,
        }
        return redirect('ConfessionsApp:questions')

def question(request, q_id):
    question = Question.objects.get(id=q_id)
    Posts = Post.objects.filter(question=question)
    context = {
        "Question": question,
        "Posts": Posts,
    }
    return render(request, "ConfessionsApp/question.html", context)

def confessions(request):
    if request.method != "POST":
        from datetime import date
        Confessions = Confession.objects.all().order_by('-date')
        print(Confessions[0].num_days_ago)
        print(Confessions[0].date)
        print(date.today())
        context = {
            "Confessions": Confessions,
        }
        return render(request, "ConfessionsApp/confessions.html", context)
    else:
        confession = Confession.objects.create(body=request.POST["ConfessionInput"], owner=request.user)
        Confessions = Confession.objects.all().order_by('-date')
        context = {
            "Confessions": Confessions,
        }
        return redirect('ConfessionsApp:confessions')

def privacy(request):
    return render(request, "ConfessionsApp/privacy.html")

def about(request):
    return render(request, "ConfessionsApp/about.html")
