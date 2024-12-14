from django.contrib import admin
from app_test.models import Test, Question, Answer, TestTry


class AnswerInlineModel(admin.TabularInline):
    model = Answer
    extra = 4
    fields = ('number', 'short_answer', 'full_answer', 'linked_question', 'is_true', 'owner')


class QuestionAdmin(admin.ModelAdmin):
    fields = ('name', 'body', 'linked_test', 'owner')
    inlines = (AnswerInlineModel,)


admin.site.register(Test)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
admin.site.register(TestTry)
