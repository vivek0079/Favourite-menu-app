from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from .utils import code_generator
from django.core.mail import send_mail
from django.urls import reverse


User = settings.AUTH_USER_MODEL

class ProfileManager(models.Manager):
    def toggle_follow(self, requested_user, user_to_toggle):
        profile_ = Profile.objects.get(user__username__iexact=user_to_toggle)
        user = requested_user
        is_following  = False
        if user in profile_.followers.all():
            profile_.followers.remove(user)
        else:
            profile_.followers.add(user)  
            is_following = True          
        return profile_, is_following


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    followers = models.ManyToManyField(User, related_name='is_following', blank=True)
    # following = models.ManyToManyField(User, related_name='following', blank=True)
    activation_key = models.CharField(max_length=120, blank=True, null=True)
    activated = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = ProfileManager()

    def __str__(self):
        return self.user.username

    def send_activation_email(self):
        if not self.activated:
            self.activation_key = code_generator()
            self.save()
            path_ = reverse('activate', kwargs={"code": self.activation_key})
            subject = 'Activate Account'
            from_email = settings.DEFAULT_FROM_EMAIL
            message = 'Activate from here: { path_ }'
            recipient_list = [self.user.email]
            html_message = '<h1>This is my HTML test path_</h1>'
            sent_mail = send_mail(subject, message, from_email, recipient_list, fail_silently=False, html_message=html_message)
            return sent_mail


def post_save_user_receiver(sender, instance, created, *args, **kwargs):
    if created:
        profile, is_created = Profile.objects.get_or_create(user=instance)
        # To make the user by default follow the admin of the site
        default_user = Profile.objects.get_or_create(user__id=1)[0]
        default_user.followers.add(instance)
        profile.followers.add(default_user.user)
        
post_save.connect(post_save_user_receiver, sender=User)
