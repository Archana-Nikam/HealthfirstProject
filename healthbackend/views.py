from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status, permissions
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from .models import Blog, Quiz, TherapistBooking, QuizResponse, Answer, TrendingSearch
from .serializers import (
    TrendingSearchSerializer,
    UserProfileSerializer,
    BlogSerializer,
    QuizSerializer,
    QuizResponseSerializer,
    TherapistBookingSerializer
)

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
# BLOG CRUD
# --------------------------
@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def create_blog(request):
    serializer = BlogSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(author=request.user if request.user.is_authenticated else None)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def list_blogs(request):
    blogs = Blog.objects.all().order_by('-created_at')
    serializer = BlogSerializer(blogs, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def get_blog(request, pk):
    try:
        blog = Blog.objects.get(pk=pk)
        serializer = BlogSerializer(blog)
        return Response(serializer.data)
    except Blog.DoesNotExist:
        return Response({'error': 'Blog not found'}, status=status.HTTP_404_NOT_FOUND)

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

@api_view(['DELETE'])
@permission_classes([permissions.AllowAny])
def delete_blog(request, pk):
    try:
        blog = Blog.objects.get(pk=pk)
        blog.delete()
        return Response({'message': 'Blog deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    except Blog.DoesNotExist:
        return Response({'error': 'Blog not found'}, status=status.HTTP_404_NOT_FOUND)

# --------------------------
# QUIZ CRUD
# --------------------------
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

# --------------------------
# QUIZ RESPONSE & FEEDBACK
# --------------------------
@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def submit_quiz_response(request):
    serializer = QuizResponseSerializer(data=request.data)
    if serializer.is_valid():
        instance = serializer.save()
        return Response({
            'message': 'Quiz submitted successfully',
            'score': serializer.get_score(instance),
            'feedback': serializer.get_feedback(instance)
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def get_quiz_feedback_by_score(request, score):
    score = int(score)
    if score >= 16:
        feedback = "You’re highly self-aware and emotionally intelligent. Keep it up!"
    elif score >= 10:
        feedback = "You have moderate emotional awareness. Consider focusing on areas that challenge you."
    else:
        feedback = "It may help to reflect more deeply or seek support to grow emotional insight."
    return Response({'score': score, 'feedback': feedback})

# --------------------------
# THERAPIST BOOKING CRUD
# --------------------------
@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def book_therapist(request):
    serializer = TherapistBookingSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            "message": "Booking submitted successfully!",
            "booking": serializer.data
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def list_therapist_bookings(request):
    bookings = TherapistBooking.objects.all().order_by('-submitted_at')
    serializer = TherapistBookingSerializer(bookings, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def get_therapist_booking(request, pk):
    try:
        booking = TherapistBooking.objects.get(pk=pk)
        serializer = TherapistBookingSerializer(booking)
        return Response(serializer.data)
    except TherapistBooking.DoesNotExist:
        return Response({'error': 'Booking not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
@permission_classes([permissions.AllowAny])
def update_therapist_booking(request, pk):
    try:
        booking = TherapistBooking.objects.get(pk=pk)
        serializer = TherapistBookingSerializer(booking, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except TherapistBooking.DoesNotExist:
        return Response({'error': 'Booking not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
@permission_classes([permissions.AllowAny])
def delete_therapist_booking(request, pk):
    try:
        booking = TherapistBooking.objects.get(pk=pk)
        booking.delete()
        return Response({'message': 'Booking deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    except TherapistBooking.DoesNotExist:
        return Response({'error': 'Booking not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def list_trending_keywords(request):
    trending = TrendingSearch.objects.all()
    serializer = TrendingSearchSerializer(trending, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def blogs_by_trending_keyword(request, keyword):
    blogs = Blog.objects.filter(title__icontains=keyword) | Blog.objects.filter(content__icontains=keyword)
    serializer = BlogSerializer(blogs, many=True)
    return Response(serializer.data)