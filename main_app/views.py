from django.db.models import fields
from django.shortcuts import render, redirect
from django.urls import reverse
# Create your views here.
from .models import Videogame, Level

# import the class that will handle basic views
from django.views import View
# import httpresponse so django knows what type of response to send
from django.http import HttpResponse

# import view class for templates
from django.views.generic.base import TemplateView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView




# Create your views here.
class VideogameCreate(CreateView):
  model = Videogame
  fields = ['name', 'img', 'bio', 'retro_videogame']
  template_name = "videogame_create.html"
  success_url = "/videogames/"

class VideogameDetail(DetailView):
  model = Videogame
  template_name = "videogame_detail.html"    

class VideogameUpdate(UpdateView):
    model = Videogame
    fields = ['name', 'img', 'bio', 'retro_videogame']
    template_name = "videogame_update.html"

    def get_success_url(self):
        return reverse('videogame_detail', kwargs={'pk': self.object.pk})    

class VideogameDelete(DeleteView):
    model = Videogame
    template_name = "videogame_delete_confirmation.html"
    success_url = "/videogames/"


# define our view

class Home(TemplateView):
  template_name = 'home.html' 


class About(TemplateView):
  template_name = 'about.html'

  


class VideogameList(TemplateView):
  template_name = 'videogame_list.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    name = self.request.GET.get("name")
    if name != None:
      context["videogames"] = Videogame.objects.filter(name__icontains=name)
      context["header"] = f"Searching for name {name}"
    else:
      context["videogames"] = Videogame.objects.all()
      context["header"] = "Videogames" 
    return context


class LevelCreate(View):

  def post(self, request, pk):
    # get the form data 
    # all form data is stored inside the request.POST
    title = request.POST.get("title")
    element = request.POST.get("element")
    boss = request.POST.get("boss")
    # get the correct artist for our connection 
    videogame = Videogame.objects.get(pk=pk)
    # create a song 
    Level.objects.create(title=title, element=element, videogame=videogame, boss=boss)
    # redirect to the proper artist page
    return redirect("videogame_detail", pk=pk)

class LevelDelete(DeleteView):
  model = Level
  success_url = "/videogames/<int:pk>/"    
