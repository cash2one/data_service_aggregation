from django.conf.urls import url, patterns

urlpatterns = patterns('person_invoice.views',
    url(r'/invoice/$', 'invoice'),
    url(r'/invoice/title/$', 'invoice_title'),
    url(r'/invoice/applyit/$', 'invoice_applyit'),
)