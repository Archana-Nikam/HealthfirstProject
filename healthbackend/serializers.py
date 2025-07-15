import logging
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Blog, Quiz, Question, QuizResponse, Answer

logger = logging.getLogger(__name__)

# ------------------------
# User Registration Serializer
# ------------------------
class UserProfileSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        return User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password']
        )

# ------------------------
# Blog Serializer
# ------------------------
class BlogSerializer(serializers.ModelSerializer):
    author_name = serializers.SerializerMethodField()
    author = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        required=False,
        allow_null=True
    )

    class Meta:
        model = Blog
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']

    def get_author_name(self, obj):
        try:
            if obj.show_author_name and obj.author:
                return obj.author.username
        except Exception as e:
            logger.warning(f"Author name fetch failed: {e}")
        return "Anonymous"

    def create(self, validated_data):
        author = validated_data.get('author', None)
        if not author:
            logger.warning("Author not provided. Blog will be anonymous.")
        return super().create(validated_data)

# ------------------------
# Quiz & Question Serializers
# ------------------------
class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

class QuizSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)

    class Meta:
        model = Quiz
        fields = ['id', 'name', 'created_at', 'questions']

    def create(self, validated_data):
        questions_data = validated_data.pop('questions')
        quiz = Quiz.objects.create(**validated_data)
        for question_data in questions_data:
            Question.objects.create(quiz=quiz, **question_data)
        return quiz

    def update(self, instance, validated_data):
        questions_data = validated_data.pop('questions', None)
        instance.name = validated_data.get('name', instance.name)
        instance.save()

        if questions_data:
            instance.questions.all().delete()
            for question_data in questions_data:
                Question.objects.create(quiz=instance, **question_data)

        return instance

# ------------------------
# Answer Serializer (✅ MISSING EARLIER)
# ------------------------
class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['question', 'selected_option']

# ------------------------
# Quiz Response Serializer with Score & Feedback
# ------------------------
class QuizResponseSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True)
    score = serializers.SerializerMethodField()
    feedback = serializers.SerializerMethodField()

    class Meta:
        model = QuizResponse
        fields = ['user_name', 'quiz', 'answers', 'score', 'feedback']

    def create(self, validated_data):
        answers_data = validated_data.pop('answers')
        response = QuizResponse.objects.create(**validated_data)
        for answer_data in answers_data:
            Answer.objects.create(response=response, **answer_data)
        return response

    def get_score(self, obj):
        total_score = 0
        score_map = {
            'strongly_disagree': 0,
            'disagree': 1,
            'neutral': 2,
            'agree': 3,
            'strongly_agree': 4,
        }
        for answer in obj.answers.all():
            total_score += score_map.get(answer.selected_option, 0)
        return total_score
def get_feedback(self, obj):
    score = self.get_score(obj)

    if score < 10:
        return {
            "level": "Low",
            "message": "You may be experiencing significant stress. Please consider booking a session with a counselor.",
            "action": "book_demo",
            "redirect_to": "/book-demo/"
        }
    elif score >= 15:
        return {
            "level": "Good",
            "message": "Your mental health looks good. Stay happy!",
            "blogs": ["5 Ways to Stay Happy", "Gratitude Journaling", "The Science of Smiling"],
            "redirect_to": None
        }
    else:
        return {
            "level": "Moderate",
            "message": "You’re doing okay, but take care of yourself. You’re strong. Read about building confidence and reducing stress.",
            "resources": ["How to Be Confident", "Why Self-Doubt Is Lying to You", "You Are Stronger Than You Think"],
            "redirect_to": "/blogs/"
        }

