from django.conf.urls import url, patterns

urlpatterns = patterns('questions.views',
        #public-question
    url(r'^question/recent/$', 'qs_recent_page'),
    url(r'^question/recent/page/(?P<page>\d{1,7})/$', 'qs_recent_page'),
    
    url(r'^question/ask/$', 'qs_ask_page'),
    url(r'^question/anwser/$', 'qs_anwser'),
    
    url(r'^question/quest/$', 'qs_quest_page'),
    url(r'^question/quest/sort/(?P<sort>\d)/$', 'qs_quest_page'),
    url(r'^question/quest/sort/(?P<sort>\d)/type/(?P<type>\d{1,3})/$', 'qs_quest_page'),
    url(r'^question/quest/sort/(?P<sort>\d)/page/(?P<page>\d{1,7})/$', 'qs_quest_page'),
    url(r'^question/quest/sort/(?P<sort>\d)/type/(?P<type>\d{1,3})/page/(?P<page>\d{1,7})/$', 'qs_quest_page'),
    
    url(r'^question/show/id/(?P<id>\d{1,7})/$', 'qs_show_page'),
    url(r'^question/relative/id/(?P<id>\d{1,7})/$', 'qs_relative_page'),
    
    url(r'^question/tag/$', 'qs_tag_page'),
    url(r'^question/tag/id/(?P<id>\d{1,7})/$', 'qs_tag_quest'),
    url(r'^question/tag/id/(?P<id>\d{1,7})/page/(?P<page>\d{1,7})/$', 'qs_tag_quest'),
    
    url(r'^question/mine/$', 'qs_mine_page'),
    url(r'^question/module/qs_type/$', 'qs_module_type_page'),
    url(r'^question/module/qs_tag/$', 'qs_module_tag_page'),
)