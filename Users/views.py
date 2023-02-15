# from django.shortcuts import render, redirect
# from django.contrib.auth import login, authenticate, logout
# from django.contrib.auth.forms import UserCreationForm
# from django.urls import reverse
# from django.contrib.auth.models import User

# client = UMDCASClient(host_name="http://127.0.0.1:8000/", post_auth_route="accounts/secure")


# client = UMDCASClient(host_name="https://umd-confessions.herokuapp.com/", post_auth_route="accounts/secure")


# def cas_login(request):
#     print(client.get_login_cas_url())
#     return redirect(client.get_login_cas_url())

# def secure(request):
#     print("secure endpoint")
#     request.session['username'] = client.validate_ticket(request)
#     username = request.session['username']
    
#     if username is not None: 
#         if User.objects.filter(username=username).exists():
#             user = User.objects.filter(username=username).first()
#             login(request, user)
#         else:
#             user = User.objects.create(username=username)
#             login(request, user)
    
#     return redirect(reverse('ConfessionsApp:confessions'))

# def cas_logout(request):
#     request.session.clear()
#     return redirect('ConfessionsApp:index')

# def LogIn(request):
#     return render(request, "Users/login.html")


# def signup(request):
#     if request.method != "POST":
#         form = UserCreationForm()	
#         context = {
#             "form": form,
#         }
#         return render(request, "Users/signup.html", context)
#     else:
#         form = UserCreationForm(data=request.POST)

#         if form.is_valid():
#             new_user = form.save()
#             login(request, new_user)
#             return redirect("ConfessionsApp:index")
#     return render(request, "Users/signup.html", {"form": form})
    
# def LogOut(request):
#     logout(request)
#     return redirect("ConfessionsApp:index")
