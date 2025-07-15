# healthbackend/admin.py
from django.contrib import admin
from .models import Blog

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'is_published', 'show_author_name', 'created_at', 'updated_at')
    list_filter = ('is_published', 'show_author_name', 'created_at')
    search_fields = ('title', 'content', 'author__username')
    ordering = ('-created_at',)
