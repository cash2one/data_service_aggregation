from django.conf.urls import url, patterns

urlpatterns = patterns('person_data.views',
    url(r'/index/$', 'index_page'),
    
    url(r'/applydata/$', 'apply_data'),
    url(r'/apply/service/(?P<service_id>\d{1,7})/$', 'apply_service'),
    
    
    url(r'/ipbind/$', 'ip_bind'),
    url(r'/ipbind/save/$', 'ip_bind_save'),
    
    url(r'/mydata/$', 'mydata'),
)