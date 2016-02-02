#coding=utf-8
from util import ModuleUtils #@UnresolvedImport
import check_kit


class Result:
    def __init__(self, success=None, message=None):
        self.success = success
        self.message = message
    def to_json(self):
        return "{ 'success' : '%s' , 'message' : '%s' }" % (self.success,self.message)
    def to_xml(self):
        return ""

# Create your views here.
#服务调用  安全认证，调用，统计...
def check_security(request, args, kwargs):
    
    #服务请求参数验证
    open_id = ModuleUtils.getParam(request ,"openid")
    if open_id == None or ModuleUtils.getParam(request ,"token") == None:
        result = Result()
        result.success = False;
        result.message = '访问请求参数不合法，请参照服务请求示例！'
        return result 
    
    #openid存在检查
    user,secret = check_kit.get_user_and_secret_by_openid(open_id);
    if user == None or secret == None :
        result = Result()
        result.success = False;
        result.message = '身份认证不通过，请核对携带的认证信息！'
        return result 
    
    #服务地址解析
    service = check_kit.get_service_by_request( args, kwargs);
    if service == None :
        result = Result()
        result.success = False;
        result.message = '服务请求地址解析失败，请参照服务请求示例！'
        return result 
    
    #服务状态检查
    status,result = check_kit.check_service_status(service)
    if not status:
        return result
    
    #服务授权校验
    auth,result = check_kit.check_authorization(user,service)
    if not auth:
        return result
    
    #服务安全认证
    authen,result = check_kit.check_authentication(request,user,secret)
    if not authen:
        return result
    
    #用户余额检查
    balance,result = check_kit.check_balance(user,service)
    if not balance:
        return result

    result = Result()
    result.success = True
    result.message = service
    return result

