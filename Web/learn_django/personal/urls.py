from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'Hello'),
    #url(r'^$', views.first_page, name = 'Hello'),
    url(r'^personal$', views.square)
]
