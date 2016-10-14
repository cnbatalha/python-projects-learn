from django.http import HttpResponse

from .models import Question

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. Django")

def without(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)

def detail(request, question_id):
    return HttpResponse("You're looking question %s" % question_id)

def results(request, question_id):
    response = "you're looking results %s"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("you're voting on %s" % question_id)    