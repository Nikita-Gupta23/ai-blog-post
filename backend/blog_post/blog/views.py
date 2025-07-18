from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return render(request, 'index.html')

def user_login(request):
    
    return render(request, 'login.html')

def user_signup(request):
    if request.method=='POST':
        username= request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        repeatPassword= request.POST['repeatPassword']

        if password==repeatPassword:
            try:
                user=User.objects.create_user(user, email, password)
                user.save()
                login(request, user)
                return redirect('/')
            
            except:
                error_message='Error Creating Account'
                return render(request, 'signup.html', {'error_message':error_message})

        else:
            error_message='Passwords do not match'
            return render(request, 'signup.html',{'error_message':error_message})
    return render(request, 'signup.html')

def user_logout(request):
    pass