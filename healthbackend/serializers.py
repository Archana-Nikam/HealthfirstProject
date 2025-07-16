# serializers.py — Correct and Clean version
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Blog, Quiz, QuizResponse, Answer, Question, TherapistBooking

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'text', 'correct_answer']

class QuizSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)

    class Meta:
        model = Quiz
        fields = ['id', 'name', 'created_at', 'questions']

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['question', 'selected_option']

class QuizResponseSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True)

    class Meta:
        model = QuizResponse
        fields = ['quiz', 'user_name', 'answers']

    def create(self, validated_data):
        answers_data = validated_data.pop('answers')
        response = QuizResponse.objects.create(**validated_data)
        for ans in answers_data:
            Answer.objects.create(response=response, **ans)
        return response

    def get_score(self, instance):
        score = 0
        for answer in instance.answers.all():
            if answer.selected_option == answer.question.correct_answer:
                score += 1
        return score

    def get_feedback(self, instance):
        score = self.get_score(instance)
        if score >= 16:
            return "You’re highly self-aware and emotionally intelligent. Keep it up!"
        elif score >= 10:
            return "You have moderate emotional awareness. Consider focusing on areas that challenge you."
        else:
            return "It may help to reflect more deeply or seek support to grow emotional insight."

class TherapistBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = TherapistBooking
        fields = '__all__'
