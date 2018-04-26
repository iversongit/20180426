from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

# Create your views here.
from extend_info.models import Extend
from student.models import Student


def addExtendInfo(request,s_id):
    if request.method == "GET":
        return render(request,"addExtendInfo.html",{'s_id':s_id})
    if request.method == "POST":
        e_addr = request.POST.get("e_addr")
        e_tel =request.POST.get("e_tel")
        e_birth = request.POST.get("e_birth")
        e_des = request.POST.get("e_des")
        Extend.objects.create(
            e_addr = e_addr,
            e_tel = e_tel,
            e_birth = e_birth,
            e_des = e_des,
            s_id=s_id
        )
        # return HttpResponse("添加成功")
        return HttpResponseRedirect("/extendapp/showall")

def showAllInfo(request):
    stus = Student.objects.all()
    extinfos = Extend.objects.all()
    return render(request,"showAllInfo.html",{'stus':stus,'extinfos':extinfos})

