

from django.conf.urls import url,include

from foxmointor import views

urlpatterns = [
    url(r'api/', include('foxmointor.api_urls')),
    #url(r'^$',views.dashboard ),
    url(r'^$',views.index ),
    url(r'^dashboard/$',views.dashboard ,name='dashboard' ),
    url(r'^triggers/$',views.triggers,name='triggers' ),
    url(r'hosts/$',views.hosts ,name='hosts'),
    url(r'hosts/(\d+)/$',views.host_detail ,name='host_detail'),
    #url(r'graph/$',views.graph ,name='get_graph'),
    url(r'trigger_list/$',views.trigger_list ,name='trigger_list'),
    #url(r'client/service/report/$',views.service_data_report )

]
