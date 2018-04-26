from django.conf.urls import url

from extend_info import views

urlpatterns = [
    url(r'addextend/(?P<s_id>\d+)',views.addExtendInfo,name='extinfo'),
    url(r'showall',views.showAllInfo)
]