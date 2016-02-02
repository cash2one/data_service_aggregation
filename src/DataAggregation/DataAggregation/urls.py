"""DataMall URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from cooperate import cooper_url #@UnresolvedImport
from index import index_url #@UnresolvedImport
from price import price_url #@UnresolvedImport
from questions import quest_url #@UnresolvedImport
from reglogin import reglog_url #@UnresolvedImport
from services import serve_url #@UnresolvedImport
from trends import trend_url #@UnresolvedImport
from person_data import data_url #@UnresolvedImport
from person_finance import finance_url #@UnresolvedImport
from person_space import space_url #@UnresolvedImport
from person_work import work_url #@UnresolvedImport
from person_invoice import invoice_url #@UnresolvedImport
from person_msg import msg_url #@UnresolvedImport
from commons import common_url #@UnresolvedImport
from serve_agent import agent_url #@UnresolvedImport

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^static_resource/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.STATIC_PATH}),
	url(r'^aggregation/static/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.STATIC_PATH}),
    #cooperate
    url(r'', include(cooper_url)),
    #index
    url(r'', include(index_url)),
    #price
    url(r'', include(price_url)),
    #questions
    url(r'', include(quest_url)),
    #reglogin
    url(r'', include(reglog_url)),
    #serve_agent
    url(r'', include(agent_url)),
    #services
    url(r'', include(serve_url)),
    #trends
    url(r'', include(trend_url)),
    #commons
    url(r'', include(common_url)),
    #person_data
    url(r'^person', include(data_url)),
    #person_finance
    url(r'^person', include(finance_url)),
    #person_space
    url(r'^person', include(space_url)),
    #person_work
    url(r'^person', include(work_url)),
    #person_invoice
    url(r'^person', include(invoice_url)),
    #person_message
    url(r'^person', include(msg_url)),
]

