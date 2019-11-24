from django.shortcuts import render
from django.http import HttpResponse
from .models import Topic

# Create your views here.
def main(request):
    return HttpResponse('Main')

def login(request):
    return HttpResponse('Hello World!')

def base(request):
    return render(request, 'base.html')

def index(request):
    return render(request, 'index.html')

def topics(request):
    topics = Topic.objects.order_by('date_added')
    context = {'topics':topics}
    return render(request,'topics.html',context)

def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic':topic,'entries':entries}
    return render(request,'topic.html',context)