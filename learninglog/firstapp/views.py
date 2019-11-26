from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from .models import Topic
from django.views.decorators import csrf

import random

from . import globalparams

# Create your views here.
def login(request):
    globalparams.g_nUserID = 0
    return render(request,'login.html')

def login_post(request):
    ctx = {}
    info = {'rlt1':'UserName','rlt2':'PassWord'}
    if request.POST:
        info['rlt1'] = request.POST['username']
        info['rlt2'] = request.POST['passwd']
    if info['rlt1'] == 'Herman' and info['rlt2'] == 'liuhuan':
        ctx['rlt'] = '校验成功!'
        globalparams.g_nUserID = random.randint(10000,19999)
        print("生成userID:%d"%globalparams.g_nUserID)
        return render(request, 'index.html')
    else:
        ctx['rlt'] = '登录失败!'
        print("\n校验失败:","\n用户名：", info['rlt1'], "\n密码:", info['rlt2'])
        print("生成userID:%d" % globalparams.g_nUserID)
        return render(request, 'login.html', ctx )

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