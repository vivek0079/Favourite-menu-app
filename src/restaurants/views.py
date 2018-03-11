from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView

from .models import Restaurant
from .forms import RestaurantCreateForm

@login_required()
def restaurant_createview(request):
    form  = RestaurantCreateForm(request.POST or None)
    errors = None
    if form.is_valid():
        if request.user.is_authenticated:
            instance = form.save(commit=False)
            instance.owner = request.user
            instance.save()
            return HttpResponseRedirect("/restaurant/")
        else:
            return HttpResponseRedirect("/login/")
    if form.errors:
        errors = form.errors

    template_name = 'restaurants/form.html'
    context = {"form": form, "errors": errors}
    return render(request, template_name, context)


class RestaurantListView(ListView):  
    def get_queryset(self):
        slug = self.kwargs.get("slug")
        if slug:
            queryset = Restaurant.objects.filter(
                    Q(category__iexact=slug) |
                    Q(category__icontains=slug)
                )
        else: 
            queryset = Restaurant.objects.all()
            
        return queryset


class RestaurantDetailView(DetailView):  
    queryset = Restaurant.objects.all()


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
    