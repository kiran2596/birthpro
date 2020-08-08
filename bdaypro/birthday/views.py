from django.shortcuts import render
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from . import models
from django.urls import reverse

# Create your views here.
# SPUERUSER homebirth pwd homebirth 
class IndexView(TemplateView):
    template_name = 'index.html'


class WishView(CreateView):
    model = models.Birthwish
    fields = ('name','message','images')
    # success_url = reverse('birthday:IndexView')

class NameList(ListView):
    model = models.Birthwish
    # school_list ...return... 
    context_object_name = 'Birthwishs'
    # otherwise take auto school_list

class BirthWishView(DetailView):
    context_object_name = 'Births_detail'
    model = models.Birthwish
    template_name = 'birthday/Births_detail.html'

