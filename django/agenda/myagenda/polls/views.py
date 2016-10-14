from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. Django")

def detail(request, question_id):
    return HttpResponse("You're looking question %s" % question_id)

def results(request, question_id):
    response = "you're looking results %s"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("you're voting on %s" % question_id)    