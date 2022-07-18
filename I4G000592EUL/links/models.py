from django.db import models
from django.contrib.auth.models import User
class Links (models. Model):

 target_url: models.URLField (max_length=200)
 description: models.CharField (max_length=200)
 identifier: models.SlugField (max_length=20, blank=True, unique=True)
 author: models.ForeignKey(User, on_delete=models.CASCADE)
 created_on: models.DateTimeField
 active: models.BooleanField (default=True)
 objects = models.Manager()
 public = ActiveLinkManager()
