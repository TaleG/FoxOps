

from django.conf.urls import url,include

from foxcmdb import views

urlpatterns = [
    url(r'^asset/',views.asset ,name='asset'),
    url(r'^hostlist',views.host,name='host_list'),
    url(r'^asset_list/list/$', views.get_asset_list, name="get_asset_list"),

]