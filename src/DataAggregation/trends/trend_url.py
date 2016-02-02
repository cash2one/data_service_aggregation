from django.conf.urls import url, patterns

urlpatterns = patterns('trends.views',
        #public-trends
    url(r'^trends/$', 'trends_page'),
    url(r'^trends/page/(?P<page>\d{1,7})/$', 'trends_page'),
)