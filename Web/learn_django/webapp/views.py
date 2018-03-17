from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.views import generic
from .models import Ratings
from .models import MovieInfo

from .forms import UserForm
from django.views.generic import View
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect



#from django.views.g

def index(request):
    return HttpResponse('Awesome HTML response')

class IndexView(generic.ListView):
    template_name = 'webapp/index.html'

    #context_object_name = 'movies'
    # default is object_list

    def get_queryset(self):
        return MovieInfo.objects.all()[:5]

class DetailView(generic.DetailView):
    model = MovieInfo
    template_name = 'webapp/detail.html'
    context_object_name = 'movie'

class UserFormView(View):
    form_class = UserForm
    # what is the blueprint that you are going to use for form

    template_name = 'webapp/register.html'

    # in class based views, you can take you get and post logic and seperate it into built in functions

    def get(self, request):
        form = self.form_class(None)# by default it has no data
        return render(request, self.template_name, {'form': form})

        pass

    def post(self, request):
        form = self.form_class(request.POST)# all data gets stored in POST

        if form.is_valid():
            # take information and store in database

            # before that make checks

            user = form.save(commit=False)
            # create object from form but saved it locally

            # clean/secure data
            # ready to enter database

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username = username, password=password)

            if user is not None:

                if user.is_active:
                    login(request, user)
                    # request.user.username  = session info

                    return redirect('webapp:index')

        return render(request, self.template_name, {'form': form})
