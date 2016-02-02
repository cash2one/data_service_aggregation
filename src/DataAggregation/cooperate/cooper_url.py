from django.conf.urls import url, patterns

urlpatterns = patterns('cooperate.views',
       #public-business
    url(r'^busi_cooper/$', 'busi_cooper_page'),
)