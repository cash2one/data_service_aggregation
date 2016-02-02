#coding=utf8
from django.shortcuts import render_to_response
from django.http.response import HttpResponseRedirect
from forms import QuestionForm, AnwserForm
from django.template.context import RequestContext
from models import Question, Question_Tag, Question_Type
import ctrls
from util import DBUtils #@UnresolvedImport

# Create your views here.
def qs_recent_page(request, page = 1):
    questions = Question.objects.all() #@UndefinedVariable
    for question in questions:
        question.anwser_count = question.anwser_set.all().count();
    question_list = DBUtils.divide_page(questions,10, page)
    return render_to_response('faqs_recent.html', {'question_list':question_list},context_instance=RequestContext(request)) 


def qs_ask_page(request):
    if request.method == 'POST':
        qform = QuestionForm(request.POST);
        if qform.is_valid():
            ctrls.saveQuestionByForm(request,qform);
            return HttpResponseRedirect("/question/quest/")
    else:
        if request.user.is_authenticated():
            quest_types = Question_Type.objects.all(); #@UndefinedVariable
            return render_to_response('faqs_ask.html', {'quest_types':quest_types},context_instance=RequestContext(request))
        else:
            return HttpResponseRedirect("/login/")


def qs_quest_page(request, page=1 ,sort=0 , type=0 ): 
    questions = ctrls.getQuestionsDynamicSql( sort, type )
    question_list = DBUtils.divide_page(questions , 10, page)
    return render_to_response('faqs_questions.html',{'question_list':question_list , 'sort' : sort ,'type' : type},context_instance=RequestContext(request))
 

def qs_show_page(request, *args, **kwargs):
    showId = kwargs.pop('id', None)
    if showId != None:
        question = Question.objects.get(id=int(showId)) #@UndefinedVariable
        return render_to_response('faqs_qshow.html',
                                  {'question':question, 'anwsers':question.anwser_set.all(), 'islogined' :request.user.is_authenticated() },
                                  context_instance=RequestContext(request))


def qs_relative_page(request, *args, **kwargs):
    showId = kwargs.pop('id', None) 
    if showId != None: 
        question = Question.objects.get(id=int(showId)) #@UndefinedVariable
        question_tags = question.tags.all()
        relatives = []   
        for question_tag in question_tags:
            re_questions = Question.objects.filter(tags=question_tag).exclude(id=showId) #@UndefinedVariable
            if(re_questions.count() > 0): 
                re_question = re_questions.order_by("-visits")[0] #从具有相同标签的问题中抽取访问量最高的作为相关问题
                re_question.anwser_count = re_question.anwser_set.all().count();
                relatives.append(re_question)
        return render_to_response('faqs_relative.html',{'relatives' : relatives },context_instance=RequestContext(request))


def qs_tag_page(request):
    question_tags = Question_Tag.objects.order_by("-visits")[0:100] #@UndefinedVariable
    return render_to_response('faqs_tags.html',{'question_tags' : question_tags },context_instance=RequestContext(request))


def qs_tag_quest(request, *args, **kwargs):
    tagId = kwargs.pop('id',None)
    page = kwargs.pop('page',1)
    if tagId != None:
        question_tag = Question_Tag.objects.get(id=int(tagId))        #@UndefinedVariable
        tag_quests = Question.objects.filter(tags=question_tag) #@UndefinedVariable
        for tag_quest in tag_quests:
            tag_quest.anwser_count = tag_quest.anwser_set.all().count();
        question_list = DBUtils.divide_page(tag_quests, 10, int(page))
    return render_to_response('faqs_tag_quest.html',{'question_list':question_list,'question_tag':question_tag},context_instance=RequestContext(request))


def qs_mine_page(request, page = 1):
    if request.user.is_authenticated():
        myQuestions = Question.objects.filter(user=request.user) #@UndefinedVariable
        for question in myQuestions:
            question.anwser_count = question.anwser_set.all().count();
        myquest_list = DBUtils.divide_page(myQuestions,10, page)
        return render_to_response('faqs_mytasks.html', {'myquest_list':myquest_list },context_instance=RequestContext(request) )
    else:
        return HttpResponseRedirect("/login/")


def qs_anwser(request):
    if request.method == 'POST':
        aform = AnwserForm(request.POST);
        if aform.is_valid():
            ctrls.saveAnwserByForm(request,aform)
            return HttpResponseRedirect("/question/show/id/%s/" % (aform.cleaned_data['anwser_qs_id']))


def qs_module_type_page(request):
    qs_types = Question_Type.objects.all(); #@UndefinedVariable
    return render_to_response('faqs_qs_type.html', {'qs_types' : qs_types},context_instance=RequestContext(request));


def qs_module_tag_page(request):
    qs_tags = Question_Tag.objects.all()[0:9]; #@UndefinedVariable
    return render_to_response('faqs_qs_tag.html', {'qs_tags' : qs_tags},context_instance=RequestContext(request));
 
