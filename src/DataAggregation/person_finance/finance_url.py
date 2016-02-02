from django.conf.urls import url, patterns

urlpatterns = patterns('person_finance.views',
    url(r'/bank/$', 'bank'),
     url(r'/bank/charge/$', 'bank_charge'),
    url(r'/buylogs/$', 'buy_logs'),
    
    url(r'/coins/$', 'coins'),
    url(r'/coins/charge/$','coins_charge'),
    
    url(r'/chargelogs/$', 'charge_logs'),
    url(r'/chargelogs/page/(?P<page>\d{1,7})/$', 'charge_logs'),
    
    url(r'/costlogs/$', 'costlogs'),
    url(r'/yhq/$', 'yhq'),
)