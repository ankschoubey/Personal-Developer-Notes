from django.conf.urls import url

from . import views

app_name = 'webapp'
urlpatterns = [
    url(r'^$', views.index, name = 'Hello'),
    url(r'^index$', views.IndexView.as_view(), name = 'index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view()),
    url(r'^register$',views.UserFormView.as_view(), name = 'register')

]
