from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.

class Paste(models.Model):
	title = models.CharField(max_length=255)
	url = models.SlugField(unique=True,max_length=255)
	content = models.TextField()
	published = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)