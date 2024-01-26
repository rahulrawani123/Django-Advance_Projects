from django.shortcuts import render
from .models import Subscription
from django.contrib import messages

# Create your views here.

def BoxOffice(request):
    if request.method=="POST":
        Name=request.POST['name']
        Movie=request.POST['movie']
        Actor=request.POST['actor']
        Actress=request.POST['actress']
        Email=request.POST['gmail']
        Genre=request.POST['genre']
        Payment=request.POST['payment']
        Subscription.objects.create(Name=Name,Movie=Movie,Actor=Actor,Actress=Actress,Email=Email,Genre=Genre,Payment=Payment)
        messages.success(request,'Hurray.... Its Almost Done Check your mail for confirm your subscription')
        
    return render(request,"Home.html")
