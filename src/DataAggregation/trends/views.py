from django.shortcuts import render_to_response
from util import DBUtils #@UnresolvedImport
from django.template.context import RequestContext
from models import Information

# Create your views here.
def trends_page(request, page = 1):
    infomations = Information.objects.all(); #@UndefinedVariable
    info_list = DBUtils.divide_page(infomations,10, page)
    return render_to_response('trends.html',{'info_list': info_list},context_instance=RequestContext(request))
