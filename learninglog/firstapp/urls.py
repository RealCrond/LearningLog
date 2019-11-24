from django.conf.urls import url,include
from . import views

urlpatterns = [
    #url(r'^$', views.main),
    url(r'^login$', views.login),
    url(r'^$', views.base, name='index'),
    url(r'^index$', views.index),
    url(r'^topics/$', views.topics, name='topics'),
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic')
]