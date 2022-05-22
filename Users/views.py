from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def LogIn(request):
    return render(request, "Users/login.html")


def signup(request):
    if request.method != "POST":
        form = UserCreationForm()	
        context = {
            "form": form,
        }
        return render(request, "Users/signup.html", context)
    else:
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect("ConfessionsApp:index")
    return render(request, "Users/signup.html", {"form": form})
    
def LogOut(request):
    logout(request)
    return redirect("ConfessionsApp:index")