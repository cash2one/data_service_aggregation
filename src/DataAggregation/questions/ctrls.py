#coding=utf8
from models import Question_Tag, Question_Type, Question, Anwser
from util import DBUtils #@UnresolvedImport

def saveQuestionByForm(request, form):
    question = Question(title=form.cleaned_data['qs_title'],
                        description=form.cleaned_data['content'],)
    
    questionType = Question_Type.objects.get(id=form.cleaned_data['qs_type']);#@UndefinedVariable
    question.type = questionType
    question.user = request.user
    question.save()
    
    tag_list = form.cleaned_data['qs_tags'].split(',');
    for tag_ele in tag_list:
        questionTag = Question_Tag.objects.filter(tag_name=tag_ele) #@UndefinedVariable
        if(questionTag.count() > 0):
            questionTag = questionTag[0]
        else:
            questionTag = Question_Tag(tag_name=tag_ele)
            questionTag.save()
        question.tags.add(questionTag)
        

def saveAnwserByForm(request, form):
    anwser = Anwser(description=form.cleaned_data['content'],)
    anwser.user = request.user;
    anwser.question = Question.objects.get(id=form.cleaned_data['anwser_qs_id']) #@UndefinedVariable
    anwser.save()
    

def getQuestionsDynamicSql(sort, type):
    operatorSql = {0:'''
                       select a.id,a.title,a.visits,a.quest_time,c.type_name,a.lastest_anwser_time,
                        count(b.id) as anwser_counts
                        from questions_question a
                        left join questions_anwser b on (a.id = b.question_id )
                        left join questions_question_type c on (a.type_id = c.id)
                        %(type_filter)s
                        group by a.id order by a.lastest_anwser_time desc
                       ''',
                   1:'''
                        select * from (
                        select t.*, sum(d.visits) as tag_vistis_counts
                         from  ( select a.id,a.title,a.visits,a.quest_time,c.type_name,a.lastest_anwser_time,
                        count(b.id) as anwser_counts
                        from questions_question a
                        left join questions_anwser b on (a.id = b.question_id )
                        left join questions_question_type c on (a.type_id = c.id)
                        %(type_filter)s
                        group by a.id )t
                        left join questions_question_tags b on (t.id = b.question_id )
                        left join questions_question_tag d on (b.question_tag_id = d.id )
                        group by t.id )s order by s.tag_vistis_counts
                       ''',
                   2:'''
                        select a.id,a.title,a.visits,a.quest_time,c.type_name,a.lastest_anwser_time,
                        count(b.id) as anwser_counts
                        from questions_question a
                        left join questions_anwser b on (a.id = b.question_id )
                        left join questions_question_type c on (a.type_id = c.id)
                        %(type_filter)s
                        group by a.id order by a.visits desc
                       ''',
                   3:'''
                       select * from (        
                        select a.id,a.title,a.visits,a.quest_time,c.type_name,a.lastest_anwser_time,
                        count(b.id) as anwser_counts
                        from questions_question a
                        left join questions_anwser b on (a.id = b.question_id )
                        left join questions_question_type c on (a.type_id = c.id)
                        %(type_filter)s
                        group by a.id ) t order by t.anwser_counts desc
                       '''
                    }
    
    if int(type) > 0 :
        type_filter = " where a.type_id =%s " % (type)
    else:
        type_filter = " "
    
    dynamicSql = operatorSql.get(int(sort)) % {'type_filter' : type_filter}
    question_list = DBUtils.executeQuerySql(dynamicSql, []);
    return question_list


