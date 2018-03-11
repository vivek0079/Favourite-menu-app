from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView

from .models import Restaurant
from .forms import RestaurantCreateForm

class RestaurantListView(LoginRequiredMixin, ListView):  
    def get_queryset(self):
        return Restaurant.objects.filter(owner=self.request.user)


class RestaurantDetailView(LoginRequiredMixin, DetailView):  
    def get_queryset(self):
        return Restaurant.objects.filter(owner=self.request.user)


class RestaurantCreateView(LoginRequiredMixin, CreateView):
    form_class = RestaurantCreateForm
    login_url = '/login/'
    template_name = "form.html"
    # success_url = "/restaurant/"

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        return super(RestaurantCreateView, self).form_valid(form)

    
    def get_context_data(self, **kwargs):
        context = super(RestaurantCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Add Restaurant'
        return context
    
class RestaurantUpdateView(LoginRequiredMixin, UpdateView):
    form_class = RestaurantCreateForm
    login_url = '/login/'
    template_name = "restaurants/detail-update.html"

    def get_context_data(self, **kwargs):
        context = super(RestaurantUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Update Restaurant'
        return context
    
    def get_queryset(self):
        return Restaurant.objects.filter(owner=self.request.user)
    