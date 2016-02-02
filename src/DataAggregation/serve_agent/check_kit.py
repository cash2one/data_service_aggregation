#coding=utf-8
from person_space.models import User_Secret #@UnresolvedImport
from django.contrib.auth.models import User
#from django.contrib.auth.hashers import make_password
from util import ModuleUtils #@UnresolvedImport
import datetime
import base64
import hashlib
import hmac
from util import RestUtils #@UnresolvedImport
import re
from person_data.models import User_data_service #@UnresolvedImport
import security
from django.core.cache import caches
from person_finance.models import User_account #@UnresolvedImport
import logging
#from passlib.handlers.pbkdf2 import pbkdf2_sha256
#from passlib.utils.pbkdf2 import pbkdf2 as passlibpbkdf2
#from django.utils.crypto import pbkdf2


logger = logging.getLogger("fileout")

def check_service_status(service):
    #检查服务是否可用
    if not service.service.status == "2":
        result = security.Result()
        result.success = False;
        result.message = '当前服务状态不可用，请联系客服人员！';
        return False, result
    return True, "";


def check_authentication(request,user,secret):
    result = security.Result()
    #用户认证校验 
    open_id = secret.open_id
    remote_addr = request.META["REMOTE_ADDR"]
    content_type = request.META["CONTENT_TYPE"]
    uri_resource = request.path
    
    #pbkdf2_sha256.encrypt("admin", salt="lxsalt", rounds=1 )
    #pbkdf2_sha256.verify("admin",passlib_hash)
    #passlibpbkdf2("admin", "lxsalt", 100, prf='hmac-sha256')
    #hash_pbkdf2 = pbkdf2("admin", "lxsalt", 100, digest=hashlib.sha256) #@UndefinedVariable
    #base64.b64encode(hash_pbkdf2).encode("utf-8")
 
    try :
        client_signature = base64.b64decode(ModuleUtils.getParam(request ,"token"))
        if not "timestamp" in client_signature:
            return False, "{'success': False,'error_message':'为防止重放攻击，请于token中加入格式为：timestamp:yyyyMMddHHmiss(24小时制)的时间戳！'}"
        timestamp = client_signature[client_signature.find("timestamp")+len("timestamp:"):];
        client_signature = client_signature[0:client_signature.find("timestamp")]
        #所传时间戳与当前时间差
        delta_seconds = (datetime.datetime.now() - datetime.datetime.strptime(timestamp, "%Y%m%d%H%M%S")).seconds
        
        stringtoSign = "%s%s%s%s%s" % (open_id,remote_addr,content_type,uri_resource,timestamp)
        server_signature = hmac.new(secret.access_Key.encode('utf-8'),
                                    stringtoSign.encode('utf-8'),
                                    digestmod=hashlib.sha256).hexdigest() #@UndefinedVariable
        #server_signature = make_password(stringtoSign ,secret.access_Key,'pbkdf2_sha256')
        #server_signature = server_signature[server_signature.rindex("$")+1:]
        if not server_signature == client_signature :
            result.success = False;
            result.message = '身份认证失败，请核对携带的认证信息！';
            return False, result
        if abs(delta_seconds) > 5*60 :
            result.success = False;
            result.message = '服务请求时间戳异常，疑似重放攻击！';
            return False, result
    except Exception,e:
        print e 
        result.success = False;
        result.message = '身份认证异常，请核对携带的认证信息！';
        return False, result
    return True, "";


def check_authorization(user,service):
    #用户授权校验
    userdatas = User_data_service.objects.filter(user__id = user.id, service_id = service.id, status = 2 )
    if userdatas.count() == 0:
        result = security.Result()
        result.success = False;
        result.message = '当前数据服务并未认证审核，如需使用请先申请数据服务，如已经审核请等待审核结果！';
        return False, result
    return True,"";


def check_balance(user,service):
    #检查账户余额
    account = User_account.objects.filter(user=user)
    if account.count() == 0:
        result = security.Result()
        result.success = False;
        result.message = '当前用户账户资料不正确，请联系客服人员！';
        return False,"";
    else:
        return True,"";


def get_user_and_secret_by_openid(open_id):
    try:
        secret = User_Secret.objects.get(open_id=open_id)
        user = User.objects.get(id=secret.user_id); #@UndefinedVariable
    except Exception :
        secret = None
        user = None
    return user,secret


def get_service_by_request( args, kwargs):
    try:
        serve_cache = caches['default']
        cate_abb = kwargs.pop('cate_abb',None)
        type_abb = kwargs.pop('type_abb',None)
        serve_abb = kwargs.pop('serve_abb',None)
        serve_cache_key = "%s-%s-%s" % ( cate_abb, type_abb, serve_abb)
    
        if None == serve_cache.get( serve_cache_key):
            paramsObj = {'service__serve_type__category__cate_abbreviation' : cate_abb,
                             'service__serve_type__type_abbreviation' : type_abb,
                             'service__serve_abbreviation' : serve_abb,
                             'recursion' : 1,
                             'page_no' : 1,
                             'page_size' : 10 }
            respObj,contentObj = RestUtils.rest_auth_get("/api_secret/",paramsObj)
            service = contentObj.results[0]
            serve_cache.set( serve_cache_key, service);
        else :
            service = serve_cache.get(serve_cache_key)
        
        regexId = "https?://.*/base/(\d)\.json"
        matchId = re.search(regexId, service.service.url)
        if matchId:
            service.service.id = matchId.group(1)
                
        regexStatus = "https?://.*/status/(\d)\.json"
        matchStatus = re.search(regexStatus, service.service.status)
        if matchStatus:
            service.service.status = matchStatus.group(1)

        return service
    except Exception,e:
        logger.info(e)
        return None
    
    