from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status, permissions
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import Quiz
from .serializers import QuizSerializer

from .models import Blog
from .serializers import BlogSerializer, UserProfileSerializer


# --------------------------
# USER REGISTRATION
# --------------------------
@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def register_user(request):
    serializer = UserProfileSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        return Response({
            'message': 'User registered successfully',
            'user': serializer.data
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# --------------------------
# ADMIN LOGIN
# --------------------------
@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def login_admin(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)

    if user and user.is_superuser:
        return Response({
            'message': 'Admin login successful',
            'username': user.username,
            'uid': user.id
        }, status=status.HTTP_200_OK)
    return Response({'error': 'Invalid admin credentials'}, status=status.HTTP_400_BAD_REQUEST)

# --------------------------
# BLOG: CREATE
# --------------------------
@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def create_blog(request):
    serializer = BlogSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(author=request.user if request.user.is_authenticated else None)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# --------------------------
# BLOG: LIST
# --------------------------
@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def list_blogs(request):
    blogs = Blog.objects.all().order_by('-created_at')
    serializer = BlogSerializer(blogs, many=True)
    return Response(serializer.data)

# --------------------------
# BLOG: GET ONE
# --------------------------
@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def get_blog(request, pk):
    try:
        blog = Blog.objects.get(pk=pk)
        serializer = BlogSerializer(blog)
        return Response(serializer.data)
    except Blog.DoesNotExist:
        return Response({'error': 'Blog not found'}, status=status.HTTP_404_NOT_FOUND)

# --------------------------
# BLOG: UPDATE
# --------------------------
@api_view(['PUT'])
@permission_classes([permissions.AllowAny])
def update_blog(request, pk):
    try:
        blog = Blog.objects.get(pk=pk)
        serializer = BlogSerializer(blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Blog.DoesNotExist:
        return Response({'error': 'Blog not found'}, status=status.HTTP_404_NOT_FOUND)

# --------------------------
# BLOG: DELETE
# --------------------------
@api_view(['DELETE'])
@permission_classes([permissions.AllowAny])
def delete_blog(request, pk):
    try:
        blog = Blog.objects.get(pk=pk)
        blog.delete()
        return Response({'message': 'Blog deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    except Blog.DoesNotExist:
        return Response({'error': 'Blog not found'}, status=status.HTTP_404_NOT_FOUND)


# api for quizz
@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def create_quiz(request):
    serializer = QuizSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def list_quizzes(request):
    quizzes = Quiz.objects.all().order_by('-created_at')
    serializer = QuizSerializer(quizzes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def get_quiz(request, pk):
    try:
        quiz = Quiz.objects.get(pk=pk)
        serializer = QuizSerializer(quiz)
        return Response(serializer.data)
    except Quiz.DoesNotExist:
        return Response({'error': 'Quiz not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
@permission_classes([permissions.AllowAny])
def update_quiz(request, pk):
    try:
        quiz = Quiz.objects.get(pk=pk)
        serializer = QuizSerializer(quiz, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Quiz.DoesNotExist:
        return Response({'error': 'Quiz not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
@permission_classes([permissions.AllowAny])
def delete_quiz(request, pk):
    try:
        quiz = Quiz.objects.get(pk=pk)
        quiz.delete()
        return Response({'message': 'Quiz deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    except Quiz.DoesNotExist:
        return Response({'error': 'Quiz not found'}, status=status.HTTP_404_NOT_FOUND)