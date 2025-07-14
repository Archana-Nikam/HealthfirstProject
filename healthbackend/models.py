from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)      
    is_published = models.BooleanField(default=True)      
     
    def __str__(self):
        return f"{self.title} by {self.author.username} on {self.created_at.strftime('%Y-%m-%d %H:%M')}"

