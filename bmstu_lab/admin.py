from django.contrib import admin
# Register your models here.
from .models import User, Test, TestResult, TestQuestion, Answer, QuestionAnswer, Question

admin.site.register(User)
admin.site.register(Test)
admin.site.register(TestResult)
admin.site.register(TestQuestion)
admin.site.register(Answer)
admin.site.register(QuestionAnswer)
admin.site.register(Question)
