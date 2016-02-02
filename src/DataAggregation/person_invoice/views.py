from django.shortcuts import render_to_response
from django.template.context import RequestContext

current_app = 'person_invoice'

def invoice(request):
    return render_to_response('invoice.html',{'current_app' : current_app,
                                              'current_tab' : request.path 
                                                   },context_instance=RequestContext(request))

def invoice_title(request):
    return render_to_response('invoice_title.html',{'current_app' : current_app,
                                                    'current_tab' : request.path 
                                                   },context_instance=RequestContext(request))

def invoice_applyit(request):
    return render_to_response('invoice_applyit.html',{'current_app' : current_app,
                                                      'current_tab' : request.path 
                                                   },context_instance=RequestContext(request))