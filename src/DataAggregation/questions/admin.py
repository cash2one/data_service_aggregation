#coding=utf8
from django.contrib import admin
from models import Question, Question_Tag, Question_Type, Anwser

# Register your models here.
admin.site.register(Question_Type)
admin.site.register(Question_Tag)

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'quest_time')
    filter_horizontal = ('tags',)
admin.site.register(Question,QuestionAdmin)

admin.site.register(Anwser)

