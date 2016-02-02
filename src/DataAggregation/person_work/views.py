from django.shortcuts import render_to_response
from django.template.context import RequestContext

current_app = 'person_work'

def work_order(request):
    return render_to_response('workorder.html',{'current_app' : current_app,
                                                'current_tab' : request.path 
                                                   },context_instance=RequestContext(request))

def workorder_submit(request):
    return render_to_response('workorder_submit.html',{'current_app' : current_app,
                                                       'current_tab' : request.path 
                                                   },context_instance=RequestContext(request))
