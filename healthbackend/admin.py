# healthbackend/admin.py
from django.contrib import admin
from .models import (
    Blog, Quiz, Question, QuizResponse, Answer,
    Therapist, TherapistBooking, TrendingSearch
)

# Custom admin for Blog
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'is_published', 'show_author_name', 'created_at', 'updated_at')
    list_filter = ('is_published', 'show_author_name', 'created_at')
    search_fields = ('title', 'content', 'author__username')
    ordering = ('-created_at',)

# Register remaining models with default admin
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(QuizResponse)
admin.site.register(Answer)
admin.site.register(Therapist)
admin.site.register(TherapistBooking)
admin.site.register(TrendingSearch)
