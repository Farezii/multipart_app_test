from django.db import models
from django.utils import timezone
from django.conf import settings

class Image(models.Model):
    image_path = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(default=timezone.now)