from django.shortcuts import render_to_response
from django.template.context import RequestContext

current_app = 'person_msg'

def msg_center(request):
    return render_to_response('msgcenter.html',{'current_app' : current_app,
                                                'current_tab' : request.path 
                                                   },context_instance=RequestContext(request))

