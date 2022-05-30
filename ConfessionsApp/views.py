from django.shortcuts import render, redirect
from .models import Question, Post, PostComment, Like, Confession
from django.db.models import Count
from django.core.paginator import Paginator

def index(request):
    return render(request, "ConfessionsApp/index.html")

def base(request):
    return render(request, "ConfessionsApp/base.html")

def questions(request):
    if request.method != "POST":
        Questions = Question.objects.all()
        context = {
            "Questions": Questions,
        }
        return render(request, "ConfessionsApp/questions.html", context)
    else:
        question = Question.objects.create(question_text=request.POST["QuestionInput"], owner=request.user)
        Questions = Question.objects.all()
        context = {
            "Questions": Questions,
        }
        return redirect('ConfessionsApp:questions')

def question(request, q_id):
    if request.method != "POST":
        question = Question.objects.get(id=q_id)
        Posts = Post.objects.filter(question=question)
        context = {
            "Question": question,
            "Posts": Posts,
        }
        return render(request, "ConfessionsApp/question.html", context)
    else:
        question = Question.objects.get(id=q_id)
        post_data = request.POST["post-input"]
        post = Post.objects.create(
            owner=request.user,
            question=question,
            post_text=post_data,
        )
        return redirect("ConfessionsApp:question", q_id=q_id)
        

def confessions(request):
    if request.method != "POST":

        SortBy = request.GET.get('SortBy') 

        if SortBy == "Newest":
            Confessions = Confession.objects.all().order_by('-date')
        elif SortBy == "Oldest":
            Confessions = Confession.objects.all().order_by('date')
        else:
            Confessions = Confession.objects.all().order_by('-date')


        paginator = Paginator(Confessions, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'ConfessionsApp/confessions.html', 
                    {'page_obj': page_obj,
                    'SortBy' : SortBy,})


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
