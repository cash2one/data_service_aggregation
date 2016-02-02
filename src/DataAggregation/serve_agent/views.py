#coding=utf-8
import datetime
import base64
import hashlib
import hmac
from django.http.response import HttpResponse
from httpproxy.views import HttpProxy
from django.utils.six.moves import urllib #@UnresolvedImport
import logging
import trans
import urllib as common_urllib

def get_test_token(request):
    open_id = "d8ngb25-n58bg-nf83-fng3-ngbgl1b435"
    access_key = "dib52kdb-3n4b51-4b5ssf-3n559sba1dfg"
    remote_addr = request.META["REMOTE_ADDR"]
    content_type = request.META["CONTENT_TYPE"]
    uri_resource = "/service/education/gdjy/gkcjcx"
    
    nowtime = datetime.datetime.strftime(datetime.datetime.now(),'%Y%m%d%H%M%S')
    stringtoSign = "%s%s%s%s%s" % (open_id,remote_addr,content_type,uri_resource,nowtime)
    test_signature = hmac.new(access_key.encode('utf-8'),
                              stringtoSign.encode('utf-8'),
                              digestmod=hashlib.sha256).hexdigest()+"timestamp:"+nowtime #@UndefinedVariable
    return HttpResponse(" 高考成绩查询服务 安全认证测试token:<br/>"
                        +"...（其中openid为用户系统id，token为生成的认证码）...<br/>"
                        +"&openid="+open_id+"<br/>&token="+base64.b64encode(test_signature))
    

logger = logging.getLogger(__name__)

class ServeAgent(HttpProxy):

    #修改此处代码，为后续扩展准备，如果是内部数据可以基于base_url来提供服务，
    #如果是调用第三方服务，这里可以根据服务提供方标识，将base_url置为"",然后直接使用url作为全路径
    def get_full_url(self, url):
        """
        Constructs the full URL to be requested.
        """
        self.request.GET._mutable = True
        self.request.GET.__delitem__("openid")
        self.request.GET.__delitem__("token")
        param_str = self.request.GET.urlencode()
        self.request.GET._mutable = False
        request_url = u'%s%s' % (self.base_url, url)
        request_url += '?%s' % param_str if param_str else ''
        return request_url

    def get(self, request, *args, **kwargs): 
        request_url = common_urllib.unquote(self.get_full_url(self.url))
        request = self.create_request(request_url)
        print "==Service invoke begin!== : %s" % datetime.datetime.now() + " ===="
        response = urllib.request.urlopen(request)
        print "==Service invoke over!== : %s" % datetime.datetime.now() + " ===="
        try:
            response_body = response.read()
            status = response.getcode()
            logger.debug(self._msg % response_body)
        except urllib.error.HTTPError as e:
            response_body = e.read()
            logger.error(self._msg % response_body)
            status = e.code
        
        if status == 200 :
            openid = kwargs.pop("openid",None)
            service = kwargs.pop("invoked_service",None)
            print "service invoke successfully : %s" % service
            user = trans.get_user_by_openid(openid)
            if not user == None and not service == None:
                trans.reduce_balance(user, service)
                trans.record_log(user, service)
        else:
            print "service invoke failed : %s" % e
        
        return HttpResponse(response_body, status=status,
                content_type=response.headers['content-type'])
