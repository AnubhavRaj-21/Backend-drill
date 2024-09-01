from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Home(request):
    #return HttpResponse("<h1>Django server</h1>")
   
    peoples = [
        {'name':"Anubhav",'age': 23}
    ]
    vegetables =['tomato','potato']
    return render(request, "index.html", context= { 'page' : 'Home'
,"peoples": peoples,'vegetables':vegetables})

def success(request):
    return HttpResponse("<h1>Suceess</h1>")