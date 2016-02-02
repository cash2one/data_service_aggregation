from django.conf.urls import url, patterns
from serve_agent.views import get_test_token #@UnresolvedImport
from serve_agent.views import ServeAgent #@UnresolvedImport
from DataAggregation import settings #@UnresolvedImport

urlpatterns = patterns("",
    url(r'^get_test_token/',get_test_token),
    url(r'^service/(?P<cate_abb>.*)/(?P<type_abb>.*)/(?P<serve_abb>.*)$', 
                        ServeAgent.as_view(base_url = settings.REAL_SERVICE_URL ) ),#mode = 'record'
)