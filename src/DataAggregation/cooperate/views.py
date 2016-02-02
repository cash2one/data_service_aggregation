from django.shortcuts import render_to_response
from forms import MessageForm
from django.http.response import HttpResponseRedirect
import ctrls
from django.template.context import RequestContext

# Create your views here.
def busi_cooper_page(request):
    if request.method == 'POST':
        msgform = MessageForm(request.POST);
        if msgform.is_valid(): 
            ctrls.saveMessageByForm(request,msgform);
            return HttpResponseRedirect("/busi_cooper/")
    else:
        return render_to_response('businesscooper.html',context_instance=RequestContext(request))