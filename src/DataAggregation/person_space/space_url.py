from django.conf.urls import url, patterns

urlpatterns = patterns('person_space.views',
                       
    url(r'/certify/$', 'certify'),
    url(r'/certify/person_apply/$', 'certify_person'),
    url(r'/certify/org_apply/$', 'certify_org'),
    
    url(r'/editpwd/$', 'edit_password'),
    url(r'/myinfo/$', 'my_info'),
    url(r'/myinfo/saveinfo/$', 'save_info'),
)