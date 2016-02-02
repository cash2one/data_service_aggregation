#coding=utf8
import httplib2
import JsonUtils

#from django.utils.six import BytesIO
#from rest_framework.parsers import JSONParser #@UnresolvedImport
#    stream = BytesIO(content)
#    data = JSONParser().parse(stream)
#    print data

default_rest_url = "http://localhost:8091/rest/service"

def rest_get(uri,params):
    if not uri.strip().startswith("http://"):
        uri = default_rest_url + uri
    h = httplib2.Http()  #httplib2.Http(".cache") 带缓存文件
    #h.add_credentials('admin', 'lx870830--') #身份验证
    if uri[-1:] == "/":
        uri = uri[:-1]
    resturi = "%s.json?%s" % (uri,dict2Str(params))
    print "[Backend request] => %s" % resturi; 
    resp, content = h.request(resturi , "GET", body="", headers={'cache-control':'no-cache'} )  
    respObj = JsonUtils.jsonStr2object(resp)
    contentObj = JsonUtils.jsonStr2object(content)
    return (respObj,contentObj)


def rest_auth_get(uri,params):
    if not uri.strip().startswith("http://"):
        uri = default_rest_url + uri
    h = httplib2.Http()  #httplib2.Http(".cache") 带缓存文件
    if uri[-1:] == "/":
        uri = uri[:-1]
    h.add_credentials('admin', 'lx870830--') #身份验证
    resturi = "%s.json?%s" % (uri,dict2Str(params))
    print "[Backend request] => %s" % resturi; 
    resp, content = h.request(resturi , "GET", body="", headers={'cache-control':'no-cache'} )  
    respObj = JsonUtils.jsonStr2object(resp)
    contentObj = JsonUtils.jsonStr2object(content)
    return (respObj,contentObj)


def dict2Str(paramsObj):
    t = ""
    for k,v in paramsObj.iteritems():
        t = t + "&%s=%s" % (k,v) 
    return t

#paramsObj = {'format':'json','page_no':1,'page_size':10}
#rest_get(default_rest_url+"/category/",paramsObj)
