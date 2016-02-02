#coding=utf8

from django.shortcuts import render_to_response
from django.template.context import RequestContext

# Create your views here.
def price_page(request):
    return render_to_response('price.html',context_instance=RequestContext(request))