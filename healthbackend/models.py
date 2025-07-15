from django.db import models
from django.contrib.auth.models import User

# ----------------------
# Blog Model
# ----------------------
class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    show_author_name = models.BooleanField(default=True)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

# ----------------------
# Quiz Models
# ----------------------

LIKERT_CHOICES = [
   
    ('agree', 'Agree'),
    ('partially_agree', 'Partially Agree'),
    ('neutral', 'Neutral'),
    ('disagree', 'Disagree'),
    
]

class Quiz(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    text = models.CharField(max_length=500)
    correct_answer = models.CharField(
        max_length=50,
        choices=LIKERT_CHOICES,
        default='neutral'  # ✅ Default value added to fix migration error
    )

    def __str__(self):
        return self.text

# ----------------------
# Quiz Response & Answer Models
# ----------------------

class QuizResponse(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='responses')
    user_name = models.CharField(max_length=255)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_name}'s response to {self.quiz.name}"

class Answer(models.Model):
    response = models.ForeignKey(QuizResponse, on_delete=models.CASCADE, related_name='answers')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_option = models.CharField(max_length=50, choices=LIKERT_CHOICES)

    def __str__(self):
        return f"{self.response.user_name} - {self.question.text} - {self.selected_option}"
