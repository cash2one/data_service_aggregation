from django.conf.urls import url, patterns

urlpatterns = patterns('person_work.views',
    url(r'/wk/$', 'work_order'),
    url(r'/wksubmit/$', 'workorder_submit'),
)