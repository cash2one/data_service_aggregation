#coding=utf8
from django.shortcuts import render_to_response

from django.template.context import RequestContext
from models import Search_Words #@UnresolvedImport
from django.core.exceptions import ObjectDoesNotExist
from questions.models import Question #@UnresolvedImport
from trends.models import Information #@UnresolvedImport
from util import RestUtils #@UnresolvedImport
from django.http.response import HttpResponseRedirect

# Create your views here.
def index_page(request):
    #服务分类展示
#    paramsObj = {'format':'json','page_no':1,'page_size':8}
#    respObj,contentObj = RestUtils.rest_get("cate_type_base", paramsObj)
#    serve_cates = contentObj.results
    infomations = Information.objects.all()[0:5]; #@UndefinedVariable
    questions = Question.objects.all()[0:5]; #@UndefinedVariable
    return render_to_response('index.html',{'infomations':infomations,
                                            'questions':questions,
                                            },context_instance=RequestContext(request))
    

def search_serve(request,servename=""):
    if servename == "" or servename == None:
        servename = request.POST.get('servename', "")
    if servename == "" or servename == None or servename.strip() == "":
        return HttpResponseRedirect("/index/")
    try:
        respObj,contentObj = RestUtils.rest_get("/base",{"serve_name__contains":servename,"recursion":1}) #@UnusedVariable
    except :
        return HttpResponseRedirect("/index/")
    searchlist = [];
    if contentObj.count > 0 :
        searchlist = contentObj.results
        try:
            searchword = Search_Words.objects.get(word=servename) #@UndefinedVariable
            searchword.visits = searchword.visits + 1
            searchword.save()
        except ObjectDoesNotExist:
            Search_Words.objects.create(word=servename) #@UndefinedVariable
    return render_to_response('api_search.html',{'searchlist':searchlist,},context_instance=RequestContext(request))


def head_content(request):
    #热点搜索列表
    visitwords = Search_Words.objects.all()[0:5] #@UndefinedVariable
    return render_to_response('head_content.html',{'visitwords':visitwords,},context_instance=RequestContext(request))
        
        
    