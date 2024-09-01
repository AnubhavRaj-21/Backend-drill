from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.messages import constants as messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/login/')
def receipes(request):
    return render(request, 'receipes.html')


def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if not User.objects.filter(username = username).exists():
            messages.info(request, "Username doesn't exist")
            return redirect('/login/')
        
        user = authenticate(username = username , password = password)
        #this return the object if the password is correct and none if it doesn't

        if username is None:
            messages.info(request, "Invalid Credentials")
            return redirect('/login/')
        else:
            login(request,user)
            return redirect('/main/')
        
    return render(request,'login.html')

def logout_page(request):
    logout(request)
    return redirect('/login/')

def register(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        if user.exists():
            messages.info(request, "Username already exists ")
            return redirect('/register/')

        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username
        )

        user.set_password(password)
        user.save()
        messages.info(request, "Accounts created successfully")
        return redirect('/register/')

