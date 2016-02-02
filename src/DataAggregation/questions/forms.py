#coding=utf8
from django import forms

#   model = Question
#   fields = ('qs_title', 'content', 'qs_tags', 'qs_type')  
#   exclude = ('title',)  
#   widgets = {
#              'name': Textarea(attrs={'cols': 80, 'rows': 20}),
#            }

class QuestionForm(forms.Form):
    qs_title = forms.CharField(max_length=100)
    content = forms.CharField(max_length=1000)
    qs_tags = forms.CharField(max_length=1000)
    qs_type = forms.IntegerField()


class AnwserForm(forms.Form):
    anwser_qs_id = forms.IntegerField()
    content = forms.CharField(max_length=1000)

