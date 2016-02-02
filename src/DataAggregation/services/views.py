#coding=utf8
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from person_data.models import User_data_service #@UnresolvedImport

# Create your views here.
def api_page(request, serveFor=""):
    return render_to_response('api.html', {'serveFor':serveFor},context_instance=RequestContext(request))


def api_list(request, sort=0, cate=0 , page=1):
    userservices = User_data_service.objects.filter(user__id = request.user.id )
    userserve_id_list = []
    for user_serve in userservices :
        userserve_id_list.append(str(user_serve.service_id));
    return render_to_response('api_list.html', {'cateid':int(cate), "userserve_id_list" : ",".join(userserve_id_list),
                                                'sortid':int(sort),
                                                'pageno':int(page),},context_instance=RequestContext(request))

def api_detail_page(request, *args, **kwargs):
    serve_id = kwargs.pop('id', None)
    return render_to_response('api_detail.html', {'serve_id':serve_id, },context_instance=RequestContext(request))


def api_detail_api(request, *args, **kwargs):
    serve_id = kwargs.pop('id', None)
    return render_to_response('api_detail_api.html', {'serve_id':serve_id,},context_instance=RequestContext(request))


def api_detail_democode(request, *args, **kwargs):
    serve_id = kwargs.pop('id', None)
    return render_to_response('api_detail_democode.html', {'serve_id':serve_id,},context_instance=RequestContext(request))


def api_detail_error(request, *args, **kwargs):
    serve_id = kwargs.pop('id', None)
    return render_to_response('api_detail_error.html', {'serve_id':serve_id,},context_instance=RequestContext(request))


def api_detail_pricelimit(request, *args, **kwargs):
    serve_id = kwargs.pop('id', None)
    return render_to_response('api_detail_pricelimit.html', {'serve_id':serve_id,},context_instance=RequestContext(request))


def api_detail_upgradelog(request, *args, **kwargs):
    serve_id = kwargs.pop('id', None)
    return render_to_response('api_detail_upgradelog.html', {'serve_id':serve_id,},context_instance=RequestContext(request))


def api_detail_others(request, *args, **kwargs):
    serve_id = kwargs.pop('id', None)
    return render_to_response('api_detail_contacts.html', {'serve_id':serve_id,},context_instance=RequestContext(request))
