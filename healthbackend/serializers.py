from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Blog

class UserProfileSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password']
        )
        return user

# ✅ Updated BlogSerializer
class BlogSerializer(serializers.ModelSerializer):
    author_name = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        fields = '__all__'

    def get_author_name(self, obj):
        if obj.show_author_name and obj.author:
            return obj.author.username
        return "Anonymous"
