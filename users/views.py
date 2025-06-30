from django.shortcuts import render
from django.http import HttpResponse# connects to the webserver database
from .forms import UserRegisterForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def user_profile(request):
    return render(request,'users/user_profile.html')

@login_required
def edit_profile(request):
    return render(request, 'users/edit_profile.html')



def signup_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # log in the user after successful signup
            return redirect('home')  # or any other page you want
    else:
        form = UserRegisterForm()
    
    return render(request, 'users/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Change to your homepage
        else:
            messages.error(request, 'Invalid credentials')
    return render(request, 'users/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')  # or home page