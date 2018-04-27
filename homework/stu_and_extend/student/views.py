from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.core.urlresolvers import reverse

from student.models import Student


def addStudent(request):
    if request.method == "GET":
        return render(request,"addStudent.html")
    if request.method == "POST":
        s_name = request.POST.get("s_name")
        s_sex = request.POST.get("s_sex")
        s_age = request.POST.get("s_age")
        s_school = request.POST.get("s_school")
        s_create_time = request.POST.get("s_create_time")

        stu = Student.objects.create(
            s_name = s_name,
            s_sex = s_sex,
            s_age = s_age,
            s_school = s_school,
            s_create_time = s_create_time
        )

        return HttpResponseRedirect(
            reverse('ext:extinfo',kwargs={'s_id':stu.id})
        )