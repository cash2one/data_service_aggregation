from django.conf.urls import url, patterns

urlpatterns = patterns('price.views',
    url(r'^price_list/$', 'price_page'),
)