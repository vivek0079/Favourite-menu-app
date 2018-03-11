from django.conf.urls import url

from .views import (
    ItemListView, 
    ItemDetailView, 
    ItemCreateView, 
    ItemUpdateView,
)

app_name = 'menus'

urlpatterns = [
    url(r'create/$', ItemCreateView.as_view(), name='create'),
    url(r'(?P<pk>\d+)/$', ItemUpdateView.as_view(), name='detail'),
    url(r'$', ItemListView.as_view(), name='list'),
]
