#coding=utf8

from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.http.response import HttpResponseRedirect, HttpResponse
from django.template.context import RequestContext
from django.contrib import auth
from forms import RegisterForm
import ctrls

def website_page(request):
    return HttpResponseRedirect("/index/")

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            #从session获取来源页面地址，进行重定向
            refer_page = request.session['login_redirect']
            if refer_page.endswith('/register/'):
                refer_page = "/index/"
            return HttpResponseRedirect(refer_page)
        else:
            return render_to_response('login.html',{'errors':'用户名或者密码不正确'}, context_instance=RequestContext(request))
    else:
        #记录来源页面地址到session
        request.session['login_redirect'] = request.META.get('HTTP_REFERER', '/')
        return render_to_response('login.html', context_instance=RequestContext(request))


def logout(request):
    auth.logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect("/index/")


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST);
        if form.is_valid():
            user = User.objects.create_inactive_user(**form.cleaned_data) #@UnusedVariable
            user = auth.authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password']) #@UnusedVariable
            auth.login(request, user)
            active_form = ctrls.generate_active_html(form.cleaned_data['username'], request.get_host()+request.path )
            ctrls.send_active_email(active_form,form.cleaned_data['email'])
            return HttpResponseRedirect("/register/active_account/")
        else:
            pass
    else:
        return render_to_response("register.html", {}, context_instance=RequestContext(request))


def active_account(request):
    if request.user.is_authenticated():
        return render_to_response("active_account.html",{'user_email':request.user.email},context_instance=RequestContext(request))
    

def active_finish(request,username,passwd):
    active_result = ctrls.check_active_url(username, passwd)
    if active_result:
        user = User.objects.get(username=username) #@UndefinedVariable
        user.is_active = True;
        user.save()
        #生成user对应的 openId和SecretAccessKey
        ctrls.generateSecret(user);
        ctrls.generateAccount(user);
    return render_to_response("active_finish.html",{'active_result':active_result},context_instance=RequestContext(request))
    
 
def check_username_duplicate(request):
    unlist = User.objects.filter(username=request.GET['username']) #@UndefinedVariable
    if unlist.count() > 0:
        return HttpResponse({'check_result': False, })
    else:
        return HttpResponse({'check_result': True, })
    
    
def check_email_duplicate(request):
    emaillist = User.objects.filter(email=request.GET['email']) #@UndefinedVariable
    if emaillist.count() > 0:
        return HttpResponse({'check_result': False, })
    else:
        return HttpResponse({'check_result': True, })
    

