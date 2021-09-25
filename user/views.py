from django.shortcuts import render
from django.http import Http404
# Create your views here.
from django.http import HttpResponse
from .models import Person
from django.template import loader

def index(request):
    # persons = Person.objects.all()
    template = loader.get_template('users/index.html')
    context = {
        'persons': Person.objects.all(),
    }
    return HttpResponse(template.render(context, request))
    # return HttpResponse(persons)

def detail(request, user_id):
    try:
        person = Person.objects.get(pk=user_id)
    except Person.DoesNotExist:
        raise Http404("Person does not exist")
    return render(request, 'users/detail.html', {'person': person})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)