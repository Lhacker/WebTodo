from django.conf.urls import url

from . import views

app_name='todo'
urlpatterns = [
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.log_out, name='logout'),
    url(r'^$', views.index, name='index'),
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/edit$', views.EditView.as_view(), name='edit'),
]
