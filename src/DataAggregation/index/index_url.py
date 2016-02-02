from django.conf.urls import url, patterns

urlpatterns = patterns('index.views',
    url(r'^index/$', 'index_page' ),
    url(r'^index/search/$', 'search_serve' ),
    url(r'^index/search/(?P<servename>.*)/$', 'search_serve' ),
    
    url(r'^head/content/$', 'head_content' ),
)