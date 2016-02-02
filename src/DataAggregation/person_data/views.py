#coding=utf-8
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from person_space.models import User_Info, User_Secret, User_Personal_Certi, User_Org_Certi  #@UnresolvedImport
from person_finance.models import User_account, User_DM_account, Cost_normal_logs #@UnresolvedImport
from person_data.models import User_data_service, IP_white_list #@UnresolvedImport
import ctrls
from util import RestUtils #@UnresolvedImport
from django.http.response import HttpResponseRedirect, HttpResponse
import json

current_app = 'person_data';

def index_page(request):
    user_info = User_Info.objects.get(user = request.user)
    user_secret = User_Secret.objects.get(user = request.user)
    person_certi = User_Personal_Certi.objects.filter(user = request.user,certi_status = 3)
    org_certi = User_Org_Certi.objects.filter(user = request.user,certi_status = 3)
    user_info.status = "未认证"
    if person_certi.count() > 0 or org_certi.count() > 0 :
        user_info.status = "已认证"
    user_account = User_account.objects.get(user = request.user)
    dm_account = User_DM_account.objects.get(user = request.user)
    userdatas = User_data_service.objects.filter(user__id = request.user.id)
    usercosts = Cost_normal_logs.objects.filter(user__id = request.user.id)
    ctrls.statistic_data_service(userdatas);
    return render_to_response('myinfo_index.html',{'current_app' : current_app,'current_tab' : request.path ,
                                                   'user_info' : user_info, 'user_secret' : user_secret, 'user_account' : user_account, 'dm_account' : dm_account,
                                                   'userdatas' : userdatas, 'usercosts' : usercosts,
                                                   },context_instance=RequestContext(request))


def apply_service(request, service_id = ""):
    if request.method == "POST" and (not service_id == "" ) :
        if not request.user.is_authenticated():
            return HttpResponse(json.dumps({ 'message' : "请先登录，登录以后才能申请服务！" }), content_type="application/json")
        userdatas = User_data_service.objects.filter(user__id = request.user.id, service_id = service_id)
        if userdatas.count() == 0 :
            User_data_service.objects.create(user = request.user, service_id = service_id, status = 1)
            return HttpResponse(json.dumps({ 'message' : "服务申请成功！" }), content_type="application/json")
        else :
            return HttpResponse(json.dumps({ 'message' : "该服务已经申请，无须重复申请！" }), content_type="application/json")
    return HttpResponse(json.dumps({ 'message' : "服务申请过程出现异常，请联系客服人员！" }), content_type="application/json")



def apply_data(request):
    return render_to_response('applydata.html',{'current_app' : current_app,
                                                'current_tab' : request.path 
                                                },context_instance=RequestContext(request))


def ip_bind(request):
    userdatas = User_data_service.objects.filter(user = request.user)
    serve_list = []
    id_list = []
    for userdata in userdatas :
        id_list.append(str(userdata.service_id))
    try:
        respObj,contentObj = RestUtils.rest_get("/base.json",{"id__in":",".join(id_list),"recursion":1}) #@UnusedVariable
        serve_list = contentObj.results
    except :
        return HttpResponseRedirect("/person/index/")
    return render_to_response('ipbind.html',{'current_app' : current_app, 'current_tab' : request.path ,
                                             'userdatas' : userdatas, 'serve_list' : serve_list,
                                              },context_instance=RequestContext(request))


def ip_bind_save(request):
    if request.method == "POST" :
        for service_id in request.POST.getlist("service_ids",[]):
            userservices = User_data_service.objects.filter(user = request.user, service_id = service_id)[0]
            ip_list = IP_white_list.objects.filter(user_service = userservices)
            ips = request.POST.get("ips","").split();
            allow_ips = ','.join(ips)
            if ip_list.count() > 0 :
                ip_list.update(allow_ips = allow_ips)
            else :
                IP_white_list.objects.create(user_service = userservices, allow_ips = allow_ips)
        return HttpResponse(json.dumps({ 'code':"0！", 'msg':"ip白名单设置成功！"}), content_type="application/json")
    return HttpResponseRedirect('/person/ipbind/')
    

def mydata(request):
    userdatas = User_data_service.objects.filter(user__id = request.user.id )
    return render_to_response('mydata.html',{'current_app' : current_app, 'userdatas' : userdatas ,
                                             'current_tab' : request.path , 'show_special_data_service' : False
                                             },context_instance=RequestContext(request))

