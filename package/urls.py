from django.conf.urls import url
from package.views import *

urlpatterns = [
    url(r'^$',CustomView.as_view(), name='custom'),
    url(r'^(?P<pk>\d+)/pack1/$', CreatePack1.as_view(), name="pack1"),
    url(r'^(?P<pk>\d+)/pack2/$', CreatePack2.as_view(), name="pack2"),
    url(r'^(?P<pk>\d+)/list/$', CustomList.as_view(), name="customList"),
    url(r'^(?P<pk>\d+)/changeCustom/$', ChangeCustom.as_view(), name="changeCustom"),
    url(r'^(?P<pk>\d+)/changePack1/$', ChangePack1.as_view(), name="changePack1"),
    url(r'^(?P<pk>\d+)/changePack2/$', ChangePack2.as_view(), name="changePack2"),
    url(r'^(?P<pk>\d+)/adminpack1/$', AdminCreatePack1.as_view(), name="adminpack1"),
    url(r'^(?P<pk>\d+)/adminpack2/$', AdminCreatePack2.as_view(), name="adminpack2"),
    url(r'^(?P<pk>\d+)/total/$', Total.as_view(), name="total"),
]