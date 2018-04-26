from django.shortcuts import render

# Create your views here.
from classroom.models import Grade


def allGrade(request):
    gs = Grade.objects.all()
    return render(request,"grade.html",{'gs':gs})

def page_not_found(request):
    return render(request,"404.html")

def server_error(request):
    return render(request,"500.html")