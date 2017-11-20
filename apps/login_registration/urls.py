
from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^users$', views.index),
    url(r'^users/$', views.index),
    url(r'^clear$',views.clear),
    url(r'^goHome$', views.goHome),
    url(r'^users/register$', views.create),
    url(r'users/login$', views.login),
    url(r'logout$', views.logout),
    ]
