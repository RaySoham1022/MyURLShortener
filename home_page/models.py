from django.db import models
from django.contrib.auth.models import User

class URLRedirection(models.Model):

    profile_username = models.CharField(max_length = 50, null = True)
    shortURL = models.URLField(null=True)
    longURL = models.URLField(null=True)




