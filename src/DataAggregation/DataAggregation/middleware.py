#coding=utf-8
'''
Created on 2009-4-9 
@author: Luox
登录认证拦截器
'''
import re
from serve_agent import security #@UnresolvedImport
from django.http import HttpResponseRedirect   
from django.http.response import HttpResponse
from util import ModuleUtils #@UnresolvedImport

class LoginAuthenticationMiddleware(object):
    def process_request(self, request):
        current_request_subject = "http://"+request.get_host()+request.get_full_path()
        regex = "https?://.+:\d{4,5}/person/.*"
        match = re.search(regex, current_request_subject)
        if match:
            if not request.user.is_authenticated():
                return HttpResponseRedirect("/login/");
        pass


class ServeAgentMiddleware(object):
    def process_view(self, request, view, args, kwargs):
        current_request_subject = "http://"+request.get_host()+request.get_full_path()
        regex = "https?://.+:\d{4,5}/service/.*/.*/.*"
        match = re.search(regex, current_request_subject)
        if match:
            result = security.check_security(request, args, kwargs)
            if result.success == False:
                return HttpResponse( result.message );
            else: 
                service = result.message
                kwargs.setdefault("url",service.serve_url)
                kwargs.setdefault("openid", ModuleUtils.getParam(request ,"openid"))
                kwargs.setdefault("invoked_service", service)
        pass
    
