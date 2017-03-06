from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.template import loader
from django.urls import reverse

from dns.rdatatype import NULL

# Create your views here.


class IndexView(generic.ListView):
    template_name = 'estudos/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        # return Question.objects.order_by('-pub_date')[:5]
        return ""
