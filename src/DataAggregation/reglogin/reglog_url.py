from django.conf.urls import url, patterns

urlpatterns = patterns('reglogin.views',
        #registerlogin-indexpage
    url(r'^$', 'website_page' ),
        #registerlogin-login
    url(r'^login/$', 'login'),
        #registerlogin-register 
    url(r'^register/$', 'register'),
    url(r'^register/check_dup_user/$', 'check_username_duplicate'),
    url(r'^register/check_dup_email/$', 'check_email_duplicate'),
    url(r'^register/active_account/$', 'active_account'),
    url(r'^register/active_finish/(?P<username>[a-zA-Z0-9]{1}([a-zA-Z0-9]|[._]){5,19})/(?P<passwd>.*)$', 'active_finish'),
)