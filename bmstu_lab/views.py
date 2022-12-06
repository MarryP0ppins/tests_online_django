from django.shortcuts import render, redirect
from .models import Test, Question, Answer, TestQuestion, QuestionAnswer

def DeleteEvent(request,id):
    Test.objects.get(id_test=id).delete()
    return redirect('/')

def GetTests(request):
    return render(request, 'tests.html', {'data':{
        'tests': Test.objects.all()
    }})

def GetTest(request, id):
    test = Test.objects.get(id_test=id)
    return render(request, 'test.html', {'data':{
        'id_test': id,
        'test': test,
        'questions': Question.objects.all(),
        'answers': Answer.objects.all(),
        'test_questions': TestQuestion.objects.all(),
        'question_answers': QuestionAnswer.objects.all()
    }})
