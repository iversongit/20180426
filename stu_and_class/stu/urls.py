from django.conf.urls import url

from stu import views

urlpatterns = [
    url(r'allstu/(\d+)',views.allStu,name="alls"),
    url(r'redirectstu/(?P<g_id>\d+)', views.redirectStu, name="restu"), # P<g_id>:指定参数名称

    # /stuapp/allstu/2018/4/1
    # url(r'selstu/(\d+)/(\d+)/(\d+)',views.selStu)
    url(r'actstu/(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)',views.actStu),
    url(r'delstu',views.delStu),
    url(r'upstu',views.upStu)
]