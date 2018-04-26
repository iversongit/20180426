from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

from django.core.urlresolvers import reverse

# Create your views here.
from stu.models import Student


def allStu(request,g_id):
    # ss = Student.objects.filter(g_id=g_id)
    # return render(request,"student.html",{"ss":ss})
    return HttpResponseRedirect(
        reverse('s:restu',kwargs={'g_id':g_id})  # stu:restu:跳转的地址， kwargs={'g_id':g_id}:向目标地址传递的参数
    )  # 请求跳转

def f(request, xxx, args, kwargs):   # args:可接收列表和元组  kwargs:可接收字典
    pass

def redirectStu(request,g_id):
    ss = Student.objects.filter(g_id=g_id)
    return render(request,"student.html",{"ss":ss})

def selStu(request,param1,param2,param3):
    return HttpResponse("传递的参数为-->"+param1+"/"+param2+"/"+param3)

def actStu(request,year,month,day):
    return HttpResponse("传递的参数为-->"+ month +"/"+day+"/"+year)

def delStu(request):  # 删除指定学生信息
    stu_id = request.GET.get('stu_id')
    Student.objects.filter(id=stu_id).delete()
    return HttpResponseRedirect("/classapp/allgrade")

def upStu(request):  # 修改指定学生信息
    stu_id = request.GET.get('stu_id')
    # stu = Student.objects.get(id=stu_id)
    # stu.s_name = "大乔"
    # stu.save()
    Student.objects.filter(id=stu_id).update(s_name='杰克')
    return HttpResponseRedirect("/classapp/allgrade")