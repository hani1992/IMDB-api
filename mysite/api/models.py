from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token



# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Movies(models.Model):
    title = models.CharField(max_length=200)
    tag = models.ManyToManyField(Tag)
    yearCreated = models.IntegerField()
    rate = models.FloatField()
    poster = models.TextField()
    trailer = models.TextField()
    IsFeatured = models.BooleanField(default=False)
    desc = models.TextField(blank=True)

    def __str__(self):
        return self.title


#create Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
