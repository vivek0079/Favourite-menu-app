from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import(
    # LoginView,
    password_reset,
    password_reset_done,
    password_reset_confirm,
    password_reset_complete
)
from restaurants.views import (
    restaurant_createview,
    RestaurantListView,
    RestaurantDetailView,
    RestaurantCreateView
)

 
urlpatterns = [
    url(r'^items/', include('menus.urls')),
    url(r'^restaurant/', include('restaurants.urls')),
    
    url(r'^password_reset/$', password_reset, name='password_reset'),
    url(r'^password_reset/done/$', password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', password_reset_complete, name='password_reset_complete'),

    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^about/$', TemplateView.as_view(template_name='about.html'), name='about'),
    url(r'^contact/$', TemplateView.as_view(template_name='contact.html'), name='contact'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    
]
