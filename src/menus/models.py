from django.db import models
from django.conf import settings
from django.urls import reverse

from restaurants.models import Restaurant

class Item(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    name = models.CharField(max_length=120)
    contents = models.TextField(help_text='Seperate each item by comma')
    excludes = models.TextField(help_text='Seperate each item by comma', blank=True, null=True)
    public = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('menus:detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-updated', '-timestamp']
        verbose_name = 'Item'
        verbose_name_plural = 'Items'                                              

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    def get_contents(self):
        return self.contents.split(",")

    def get_excludes(self):
        return self.excludes.split(",")