from django.conf.urls import url, patterns

urlpatterns = patterns('person_msg.views',
    url(r'/msgcenter/$', 'msg_center'),
)