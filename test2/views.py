from django.shortcuts import render, get_object_or_404
from django.template import loader
from .models import Question
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import Choice, Question

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'test2/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'test2/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'test2/results.html'


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'test2/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'test2/index.html', context)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'test2/results.html', {'question': question})