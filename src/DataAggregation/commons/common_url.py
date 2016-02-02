from django.conf.urls import url, patterns

urlpatterns = patterns('commons.views',
                       
    url(r'^common/location/provinces/$', 'get_province'),
    url(r'^common/location/(?P<province>\d{1,7})/citys/$', 'get_city_by_province'),
    url(r'^common/location/(?P<city>\d{1,7})/districts/$', 'get_district_by_city'),
)