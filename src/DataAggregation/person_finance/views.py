#coding=utf-8

from django.shortcuts import render_to_response
from django.template.context import RequestContext
from person_finance.models import \
Bank_account_info, Alipay_account_info, User_account, User_account_alarm, Charge_normal_logs,User_DM_account, User_coupon,Cost_type #@UnresolvedImport
from django.http.response import HttpResponse, HttpResponseRedirect
import json
from util import DBUtils #@UnresolvedImport
import math
import ctrls

current_app = 'person_finance'

def bank(request):
    bank_infos = Bank_account_info.objects.all();
    alipay_infos = Alipay_account_info.objects.all();
    account = User_account.objects.get(user=request.user)
    account_alarm = User_account_alarm.objects.get(user=request.user)
    return render_to_response('bank.html',{'current_app' : current_app,'current_tab' : request.path,
                                           'bank_infos' : bank_infos, 'alipay_infos' : alipay_infos,
                                           'account' : account, 'account_alarm' : account_alarm,
                                                   },context_instance=RequestContext(request))


def bank_charge(request):
    if request.method == "POST":
        charge_price = int(request.POST.get("charge_price",0));
        if charge_price > 0:
            user_account = User_account.objects.get(user = request.user)
            money_before = user_account.money
            money_after = money_before + charge_price;
            user_account.money =  money_after
            user_account.save()
            Charge_normal_logs.objects.create(user = request.user, account = user_account, 
                                              money_before = money_before, charge_money = charge_price,  money_after = money_after, );
            return HttpResponse(json.dumps({"result":"充值成功,充值金额为：%d元" % charge_price}), content_type="application/json")
        else :
            return HttpResponse(json.dumps({"result":"充值过程中出现异常！"}), content_type="application/json")
    return HttpResponseRedirect("/person/bank/")

    
def buy_logs(request):
    return render_to_response('buylogs.html',{'current_app' : current_app,
                                              'current_tab' : request.path 
                                                   },context_instance=RequestContext(request))


def coins(request):
    coins_price_per_rmb = 10
    dm_account = User_DM_account.objects.get(user = request.user)
    user_account = User_account.objects.get(user = request.user)
    return render_to_response('coins.html',{'current_app' : current_app,'current_tab' : request.path ,'user_account' : user_account,
                                            'dm_account' : dm_account,'coins_price_per_rmb' : coins_price_per_rmb,
                                                   },context_instance=RequestContext(request))
    

def coins_charge(request):
    if request.method == "POST":
        charge_price = int(request.POST.get("charge_price",0));
        account = User_account.objects.get(user = request.user)
        if charge_price > account.money :
            return HttpResponse(json.dumps({"code" : 1,"msg":"*余额不足，不能完成兑换!"}), content_type="application/json")
        else :
            #扣减账户金额
            ctrls.reduceAccount(request.user , charge_price);
            #计算DM币账户
            ctrls.chargeDMAccount(request.user , charge_price)
            return HttpResponse(json.dumps({"code" : 0,"msg":"充值成功，充值金额为%d元！" % charge_price}), content_type="application/json")
    return HttpResponseRedirect("/person/bank/")
    

def charge_logs(request, page = "1"):
    charge_n_logs = Charge_normal_logs.objects.filter(user = request.user )
    log_list = DBUtils.divide_page(charge_n_logs, 10, int(page))
    log_list.count = int(math.ceil(charge_n_logs.count() / float( '%.2f' % 10)));
    return render_to_response('chargelogs.html',{'current_app' : current_app, 'current_tab' : request.path,
                                                 'log_list' : log_list,
                                                   },context_instance=RequestContext(request))


def costlogs(request):
    return render_to_response('costlogs.html',{'current_app' : current_app, 'cost_types' : Cost_type.objects.all(),
                                               'current_tab' : request.path 
                                                   },context_instance=RequestContext(request))


def yhq(request):
    coupon_list = User_coupon.objects.filter(user = request.user);
    return render_to_response('yhq.html',{'current_app' : current_app,'current_tab' : request.path ,
                                          'coupon_list' : coupon_list,
                                                   },context_instance=RequestContext(request))
    
    