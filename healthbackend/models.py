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

LIKE_CHOICES = [
   
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
        choices=LIKE_CHOICES,
        default='neutral'  
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
    selected_option = models.CharField(max_length=50, choices=LIKE_CHOICES)

    def __str__(self):
        return f"{self.response.user_name} - {self.question.text} - {self.selected_option}"

# for booking therpist model
THERAPY_TYPE_CHOICES = [
   
    ('student', 'Student'),
    ('couple', 'Couple'),
    ('cbt', 'Cognitive Behavioral Therapy'),
    ('mindfulness', 'Mindfulness Therapy'),
    ('talk', 'Talk Therapy'),
]

GENDER_IDENTITY_CHOICES = [
    ('male', 'Male'),
    ('female', 'Female'),
   
    ('prefer_not_say', 'Prefer not to say'),
]



# Therapist Model
class Therapist(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    specialization = models.CharField(max_length=100)
    location = models.CharField(max_length=100)  
    available_days = models.CharField(max_length=100)
    available_time = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} - {self.specialization}"


# Therapist Booking Model (linked to Therapist)
class TherapistBooking(models.Model):
    therapist = models.ForeignKey(
        Therapist,
        on_delete=models.SET_NULL,   
        null=True,
        blank=True,
        related_name='bookings'
    )
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    therapy_type = models.CharField(max_length=20, choices=THERAPY_TYPE_CHOICES)
    pronouns = models.CharField(max_length=100, blank=True)
    age = models.PositiveIntegerField()
    gender_identity = models.CharField(max_length=20, choices=GENDER_IDENTITY_CHOICES)
    occupation = models.CharField(max_length=255)
    reason_for_therapy = models.TextField()
    preferred_time_slot = models.DateTimeField()
    payment_completed = models.BooleanField(default=False)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.therapy_type}"


class TrendingSearch(models.Model):
    keyword = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.keyword