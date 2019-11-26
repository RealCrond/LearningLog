from django.conf.urls import url,include
from . import views
from . import search

urlpatterns = [
    url(r'^$', views.login, name='login'),
    url(r'^login-post$', views.login_post),
    url(r'^base$', views.base, name='base'),
    url(r'^index$', views.index, name='index'),
    url(r'^topics/$', views.topics, name='topics'),
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    url(r'^search-form$', search.search_form),
    url(r'^search$', search.search),
    url(r'^search-post$',search.search_post,name='search_post'),
]