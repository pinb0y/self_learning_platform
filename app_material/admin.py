from django.contrib import admin

from app_material.models import Section, Material, Subscription
from app_test.models import Test, Question, Answer, TestTry

admin.site.register(Section)
admin.site.register(Material)
admin.site.register(Subscription)
admin.site.register(Test)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(TestTry)

