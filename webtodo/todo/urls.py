from django.conf.urls import url

from . import views

app_name='todo'
urlpatterns = [
    url(r'^login/$', views.login, name='login'),
    url(r'^do_login/$', views.do_login, name='do_login'),
    url(r'^$', views.index, name='index'),
]
