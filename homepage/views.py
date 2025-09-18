from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth 
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request, "index.html")

def register(request):
    if request.method == 'POST':
        # fname=request.POST["fname"]
        # lname=request.POST["lname"]
        username=request.POST["username"]
        email=request.POST["email"]
        password=request.POST["password"]
        confirm=request.POST["confirm_password"]

        if password == confirm:
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email already used")
                return redirect("register")
            elif User.objects.filter(username=username).exists():
                messages.info(request, "Username already used")
                return redirect("register")
            else:
                user = User.objects.create_user(username=username,email=email,password=password)
                user.save();
                return redirect("register")
        else:
            messages.info(request,"Your password doesn't match")
            return redirect('register')
        
    else:
        return render(request,"register.html")