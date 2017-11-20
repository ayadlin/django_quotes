
from django.conf.urls import url
from . import views
urlpatterns = [

    url(r'^$', views.index),
    url(r'^clear$',views.clear),
    url(r'^goHome$', views.goHome),
    url(r'^new_quote$',views.create_quote),
    url(r'^dashboard$',views.dashboard),
    url(r'^favorite$',views.add_favorite),
    url(r'^not_favorite$',views.remove_favorite),
    url(r'^user/(?P<user_id>\d+)$',views.view_user_quotes),
    url(r'^(?P<user_id>\d+)$',views.view_user_quotes), # just in case of typo

]



