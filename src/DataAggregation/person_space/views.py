#coding=utf-8

from django.shortcuts import render_to_response
from django.template.context import RequestContext
from person_space.models import User_Info, User_Personal_Certi, User_Org_Certi, User_Secret #@UnresolvedImport
from forms import UserInfoForm, EditPasswordForm, PersonalCertiFrom, OrgCertiFrom
from django.http.response import HttpResponseRedirect, HttpResponse
from django.contrib import auth
import json
import datetime


current_app = 'person_space'

def certify(request):
    cur_user = request.user
    person_certi = User_Personal_Certi.objects.filter(user=cur_user)
    if person_certi.count() > 0:
        person_certi = person_certi[0]
    org_certi = User_Org_Certi.objects.filter(user=cur_user)
    if org_certi.count() > 0:
        org_certi = org_certi[0]
    return render_to_response('certify.html',{'current_app' : current_app,'current_tab' : request.path,
                                              'person_certi' : person_certi, 'org_certi' : org_certi,
                                                   },context_instance=RequestContext(request))


CERTI_PASS_MESSAGE = { 'result':"认证信息已经成功提交，请等待审核(10个工作日内)！"}
CERTI_WAIT_MESSAGE = { 'result':"正在审核处理中，请等待审核结果！"}
CERTI_IDENTIFICATION_MESSAGE = { 'result':"认证信息已经成功提交，请等待审核(10个工作日内)！"}
CERTI_VALIDFAIL_MESSAGE = { 'result':"认证信息验证不正确，请重新核对！"}

def certify_person(request):
    if request.method == "POST":
#        上传文件使用request.FILES["xx"]来接收，另外html表单form必须设置enctype="multipart/form-data"属性
        certiform = PersonalCertiFrom(request.POST, request.FILES)
        if certiform.is_valid() :
            certi_record = User_Personal_Certi.objects.filter(user = request.user )
            if not certi_record.count() > 0 :
                certi_person = User_Personal_Certi( user = request.user, certi_time = datetime.datetime.now(), certi_status = 0, **certiform.cleaned_data )
                certi_person.save()
                return HttpResponse(json.dumps(CERTI_PASS_MESSAGE), content_type="application/json")
            else:
                if certi_record[0].certi_status == 0:
                    return HttpResponse(json.dumps(CERTI_WAIT_MESSAGE), content_type="application/json")
                else :
                    if certi_record[0].certi_status == 1:
                        return HttpResponse(json.dumps(CERTI_IDENTIFICATION_MESSAGE), content_type="application/json")
                    else :
                        if certi_record[0].certi_status == 2:
                            certi_record.update(certi_status = 0, modify_time = datetime.datetime.now() ,**certiform.cleaned_data)
        else:
            return HttpResponse(json.dumps(CERTI_VALIDFAIL_MESSAGE), content_type="application/json")
    return HttpResponseRedirect("/person/certify/")


def certify_org(request):
    if request.method == "POST":
#        上传文件使用request.FILES["xx"]来接收，另外html表单form必须设置enctype="multipart/form-data"属性
        certiform = OrgCertiFrom(request.POST,  request.FILES)
        if certiform.is_valid() :
            certi_record = User_Org_Certi.objects.filter(user = request.user )
            if not certi_record.count() > 0 :
                certi_org = User_Org_Certi( user = request.user, certi_time = datetime.datetime.now(), certi_status = 0, **certiform.cleaned_data )
                certi_org.save()
                return HttpResponse(json.dumps(CERTI_PASS_MESSAGE), content_type="application/json")
            else:
                if certi_record[0].certi_status == 0:
                    return HttpResponse(json.dumps(CERTI_WAIT_MESSAGE), content_type="application/json")
                else :
                    if certi_record[0].certi_status == 1:
                        return HttpResponse(json.dumps(CERTI_IDENTIFICATION_MESSAGE), content_type="application/json")
                    else :
                        if certi_record[0].certi_status == 2:
                            certi_record.update(certi_status = 0, modify_time = datetime.datetime.now() ,**certiform.cleaned_data)
        else:
            return HttpResponse(json.dumps(CERTI_VALIDFAIL_MESSAGE), content_type="application/json")
    return HttpResponseRedirect("/person/certify/")


def edit_password(request):
    if request.method == "POST":
        form = EditPasswordForm(request.POST)
        if form.is_valid():
            user = auth.authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['oldPassword']) #@UndefinedVariable
            if (not user == None) and user.is_active and user.is_authenticated() :
                user.set_password(form.cleaned_data['newPassword'])
                user.save()
                auth.login(request, user)
                return HttpResponse(json.dumps({ 'result':"密码修改成功！"}), content_type="application/json") 
            else :
                return HttpResponse(json.dumps({ 'result':"输入的原密码不正确！"}), content_type="application/json")   
    else :
        return render_to_response('editpwd.html',{'current_app' : current_app, 'current_tab' : request.path 
                                                   },context_instance=RequestContext(request))


def my_info(request):
    cur_user = request.user
    user_info = User_Info.objects.filter(user=cur_user)
    if user_info.count() > 0:
        user_info = user_info[0]
    user_secret = User_Secret.objects.get(user=cur_user)
    return render_to_response('myinfo.html',{ 'current_app' : current_app, 'current_tab' : request.path,
                                              'user_info' : user_info, 'user_secret' : user_secret,
                                                   },context_instance=RequestContext(request))


def save_info(request):
    if request.method == 'POST':
        form = UserInfoForm(request.POST)
        if form.is_valid():
            #form.cleaned_data["xx"] mobile_no, nickname, user_type
            user_info = User_Info(user = request.user, **form.cleaned_data) 
            user_info.save()
    return HttpResponseRedirect("/person/myinfo/")


