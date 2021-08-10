from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from polls.models import *

def home(request):
    context = {
        'questions': Question.objects.all(),
    }
    return render(request, 'polls/index.html', context)

def details(request, id):
    context = {
        'question': get_object_or_404(Question, pk=id)
    }
    return render(request, 'polls/details.html', context)

def vote(request, id):
    choice_id = request.POST['choice']
    question = Question.objects.get(pk=id)
    choice = question.choice_set.get(pk=choice_id)
    choice.votes += 1
    choice.save()
    return HttpResponseRedirect(reverse('polls-results', args=(id,)))

def results(request, id):
    try:
        context = {
            'question': Question.objects.get(pk=id)
        }
    except:
        raise Http404()
    return render(request, 'polls/results.html', context)