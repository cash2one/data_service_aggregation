#coding=utf8
from models import MessageBoard #@UnresolvedImport

def saveMessageByForm(request, form):
    MessageBoard.objects.create(**form.cleaned_data) #@UndefinedVariable