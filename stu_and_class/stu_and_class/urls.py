"""stu_and_class URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from classroom.views import page_not_found,server_error

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^stuapp/',include('stu.urls',namespace='s')),
    url(r'^classapp/',include('classroom.urls'))
]

handler404 = page_not_found  # handler404:django指定处理404错误的关键字   适用情况：网页找不到
handler500 = server_error    # handler500:django指定处理500错误的关键字  适用情况：代码错误
