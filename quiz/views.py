from django.shortcuts import render, get_object_or_404, render_to_response
from django.shortcuts import redirect
from django.utils import timezone
from .models import Quiz
from .models import Question
from .models import Option
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect

def quiz_detail(request, pk):
    quiz = get_object_or_404(Quiz, pk=pk)
    questions = Question.objects.all()
    question = get_object_or_404(Question, pk=pk)
    options = Option.objects.all()
    option = get_object_or_404(Option, pk=pk)
    return render(request, 'quiz/quiz_detail.html', {'quiz': quiz, 'questions': questions, 'question': question, 'options': options, 'option': option})
	
	
def quiz_list(request):
    quizs = Quiz.objects.all()
    return render(request, 'quiz/quiz_list.html', {'quizs': quizs})	


def question_detail(request, pk):
    question = get_object_or_404(Question)
    return render(request, 'quiz/question_detail.html', {'question': question})
	
	
def question_list(request):
    questions = Question.objects.all()
    return render(request, 'quiz/question_list.html', {'questions': questions})	

def option_detail(request, pk):
    option = get_object_or_404(Option)
    return render(request, 'quiz/option_detail.html', {'option': option})
	
	
def option_list(request):
    options = Option.objects.all()
    return render(request, 'quiz/option_list.html', {'options': options})	


