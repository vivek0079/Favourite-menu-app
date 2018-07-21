from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView

from django.contrib.auth.views import(
    password_reset,
    password_reset_done,
    password_reset_confirm,
    password_reset_complete
)
from profiles.views import ProfileFollow, RegisterView
 
urlpatterns = [
    url(r'^items/', include('menus.urls')),
    url(r'^restaurant/', include('restaurants.urls')),
    url(r'^users/', include('profiles.urls')),
    
    url(r'^password_reset/$', password_reset, name='password_reset'),
    url(r'^password_reset/done/$', password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', password_reset_complete, name='password_reset_complete'),

    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^follow/$', ProfileFollow.as_view(), name='follow'),
    
]
