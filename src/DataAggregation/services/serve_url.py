from django.conf.urls import url, patterns

urlpatterns = patterns('services.views',
    url(r'^API/$', 'api_page'),
    url(r'^API/hotservice/$', 'api_page', {'serveFor':'hotservice'}),
    url(r'^API/latestservice/$', 'api_page', {'serveFor':'latestservice'}),
    
    url(r'^API/cate/(?P<cate>\d{1,3})/$', 'api_list'),
    url(r'^API/cate/(?P<cate>\d{1,3})/sort/(?P<sort>\d)/$', 'api_list'),
    url(r'^API/cate/(?P<cate>\d{1,3})/sort/(?P<sort>\d)/page/(?P<page>\d{1,7})/$', 'api_list'),
    
    url(r'^API/detail/id/(?P<id>\d{1,7})/$', 'api_detail_page'),
    url(r'^API/detail/api/id/(?P<id>\d{1,7})/$', 'api_detail_api'),
    url(r'^API/detail/democode/id/(?P<id>\d{1,7})/$', 'api_detail_democode'),
    url(r'^API/detail/error/id/(?P<id>\d{1,7})/$', 'api_detail_error'),
    url(r'^API/detail/pricelimit/id/(?P<id>\d{1,7})/$', 'api_detail_pricelimit'),
    url(r'^API/detail/upgradelog/id/(?P<id>\d{1,7})/$', 'api_detail_upgradelog'),
    url(r'^API/detail/others/id/(?P<id>\d{1,7})/$', 'api_detail_others'),
)