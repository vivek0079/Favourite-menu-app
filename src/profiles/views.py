from django.contrib.auth import get_user_model
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView

from restaurants.models import Restaurant
from menus.models import Item

User = get_user_model()

class ProfileDetailView(DetailView):
    template_name = 'profiles/user.html'

    def get_object(self):
        username = self.kwargs.get("username")
        if username is None:
            raise Http404
        return get_object_or_404(User, username__iexact=username, is_active=True)

    def get_context_data(self, **kwargs):
        context = super(ProfileDetailView, self).get_context_data(**kwargs)
        user = context['user']
        query = self.request.GET.get('q')
        item_exists = Item.objects.filter(user=user).exists()
        qs = Restaurant.objects.filter(owner=user)
        if query:
            qs = qs.search(query)         
        if item_exists and qs.exists():
            context['locations'] = qs
        return context