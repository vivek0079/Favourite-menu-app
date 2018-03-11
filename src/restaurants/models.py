from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save, post_save
from django.urls import reverse

from .utils import unique_slug_generator
from .validators import validate_category

User = settings.AUTH_USER_MODEL

class Restaurant(models.Model):
    """Model definition for Restaurant."""
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    location = models.CharField(max_length=120, blank=True, null=True)
    category = models.CharField(max_length=120, blank=True, null=True, validators=[validate_category])
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(blank=True, null=True)


    class Meta:
        """Meta definition for Restaurant."""

        verbose_name = 'Restaurant'
        verbose_name_plural = 'Restaurants'

    def __unicode__(self):
        """Unicode representation of Restaurant."""
        return (self.name)
 
    def __str__(self):
        return (self.name)
    
    def get_absolute_url(self):
        return reverse('restaurants:detail', kwargs={'slug': self.slug})

    # def get_absolute_url(self):
    #     from django.core.urlresolvers import reverse
    #     return reverse('', kwargs={'pk': self.pk})
    @property
    def title(self):
        return self.name
    
def pre_save_receiver(sender, instance, *args, **kwargs):
    instance.category = instance.category.capitalize()
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


# def post_save_receiver(sender, instance, created, *args, **kwargs):
#     print('saved')
#     print(instance.timestamp)
#     if not instance.slug:
#         instance.slug = unique_slug_generator(instance)
#         instance.save()

pre_save.connect(pre_save_receiver, sender=Restaurant)
# post_save.connect(post_save_receiver, sender=Restaurant)