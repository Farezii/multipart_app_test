from django.contrib import admin
from .models import Image

class ImageAdmin(admin.ModelAdmin):
    list_display = ('given_id', 'image_path', 'created_at')
    search_fields = ('given_id', 'created_at')
    list_filter = ('created_at',)
    ordering = ('-created_at',)
    
admin.site.register(Image, ImageAdmin)