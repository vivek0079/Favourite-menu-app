from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView, DetailView, View

from restaurants.models import Restaurant
from menus.models import Item
from .models import Profile
from .forms import RegisterForm


User = get_user_model()

def activate_user_view(request, code=None, *args, **kwargs):
    if code:
        qs = Profile.objects.filter(activation_key=code)
        if qs.exists() and qs.count() == 1:
            profile = qs.first()
            if not act_obj.activated:
                user_ = profile.user
                user_.is_active = True
                user_.save()
                profile.activated = True
                profile.activation_key = None
                profile.save()
                return redirect("/login")
    # invalid code
    return redirect("/login")



class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = "registration/register.html"
    success_url = '/'

    def dispatch(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("/logout")
        return super(RegisterView, self).dispatch(*args, **kwargs)

class ProfileFollow(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        user_to_toggle = request.POST.get("username")
        profile_, is_following = Profile.objects.toggle_follow(request.user, user_to_toggle)
        return redirect('/users/Vivek')


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
        is_following = False
        if user.profile in self.request.user.is_following.all():
            is_following = True
        context['is_following'] = is_following
        query = self.request.GET.get('q')
        item_exists = Item.objects.filter(user=user).exists()
        qs = Restaurant.objects.filter(owner=user)
        if query:
            qs = qs.search(query)         
        if item_exists and qs.exists():
            context['locations'] = qs
        return context