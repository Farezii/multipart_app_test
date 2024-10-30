from django.db import models
from django.utils import timezone
from django.conf import settings

class Image(models.Model):
    given_id = models.CharField(max_length=150)
    image_path = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(default=timezone.now)