from django.contrib import admin

# Register your models here.
from .models import Blog

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'updated_at', 'is_published')
    search_fields = ('title', 'content', 'author__username')
    list_filter = ('created_at', 'is_published')