from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from .models import User

# Create your views here.
def signup(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        repeatpassword = request.POST.get('repeatpassword', '')

        if name and email and password and repeatpassword:
            user = User.objects.create_user(name, email, password)
            print(f"user: {user}")
            return redirect('/login/')
        else:
            print("smth went wrong")
    else:
        print("show the form")
    return render(request, "account/signup.html")

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')

        if email and password:
            user = authenticate(request, email=email, password=password)
            if user is not None:
                auth_login(request, user)
                print(request.user.is_authenticated)
                return redirect('/')


    return render(request, "account/login.html")

    
    