from django.conf.urls import url

from . import views

app_name = 'estudos'
urlpatterns = [
    # /pools/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # /pools/without
    url(r'^without/$', views.without, name='without'),    
    # /pools/5/.
    #url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # /pools/5/results/
    #url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # /pools/5/vote/
    #url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),    
]