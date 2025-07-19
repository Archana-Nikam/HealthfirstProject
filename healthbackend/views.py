from django.http import HttpResponse

def home_view(request):
    return HttpResponse("""
        <html>
        <head>
            <title>HealthFirst Backend</title>
            <style>
                body {
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    background: #f7fafc;
                    color: #333;
                    text-align: center;
                    padding: 40px;
                }
                h1 {
                    color: #37474F;
                    font-size: 2.5em;
                    margin-bottom: 10px;
                }
                p {
                    font-size: 1.2em;
                    color: #555;
                    margin-bottom: 30px;
                }
                ul {
                    list-style-type: none;
                    padding: 0;
                    margin: 0 auto;
                    max-width: 300px;
                }
                li {
                    margin: 25px 0;  
                }
                a {
                    text-decoration: none;
                    color: white;
                    padding: 12px 24px;
                    border-radius: 8px;
                    font-weight: bold;
                    transition: background 0.3s, transform 0.2s;
                    display: inline-block;
                    width: 100%;
                }
                .admin-link a {
                    background: #1976d2;
                }
                .admin-link a:hover {
                    background: #1565c0;
                    transform: scale(1.05);
                }
                .api-link a {
                    background: #388e3c;
                }
                .api-link a:hover {
                    background: #2e7d32;
                    transform: scale(1.05);
                }
            </style>
        </head>
        <body>
            <h1> Welcome to the HealthFirst Project's Backend</h1>
            <p>Available paths:</p>
            <ul>
                <li class="admin-link"><a href="/admin/"> Admin Panel</a></li>
                <li class="api-link"><a href="/api/">API Root</a></li>
            </ul>
        </body>
        </html>
    """)

def api_root_view(request):
    return HttpResponse("""
    <html>
    <head>
        <title>HealthFirst API Dashboard</title>
        <style>
            body {
                font-family: 'Segoe UI', Tahoma, sans-serif;
                background-color: #f0f4f8;
                padding: 40px;
                color: #333;
                font-size: 14px;
            }
            h1 {
                text-align: center;
                color: #1a237e;
                font-size: 2em;
                margin-bottom: 20px;
            }
            h2 {
                color: #37474f;
                font-size: 1.1em;
                margin-bottom: 12px;
            }
            .row {
                display: flex;
                justify-content: center;
                gap: 40px;
                margin-bottom: 35px;
            }
            .col {
                display: flex;
                flex-direction: column;
                gap: 20px;
            }
            .card {
                background-color: #ffffff;
                border: 1px solid #e0e0e0;
                border-radius: 12px;
                box-shadow: 0 2px 6px rgba(0, 0, 0, 0.06);
                padding: 20px;
                width: 280px;
            }
            .small-card {
                width: 280px;
            }
            .link-grid {
                display: flex;
                flex-direction: column;
                gap: 10px;
                margin-top: 10px;
            }
            .api-link {
                background-color: #dbeafe; /* soft blue */
                color: #0b3d91;
                padding: 10px;
                text-decoration: none;
                border-radius: 6px;
                font-weight: 500;
                text-align: center;
                transition: all 0.3s ease;
            }
            .api-link:hover {
                background-color: #bfdbfe;
            }
        </style>
    </head>
    <body>
        <h1>Welcome to the HealthFirst API</h1>

        <!-- Row 1: Authentication & Blogs -->
        <div class="row">
            <div class="col">
                <div class="card">
                    <h2>Authentication</h2>
                    <div class="link-grid">
                        <a href="/admin/" class="api-link">Admin Panel</a>
                        <a href="/api/register/" class="api-link">Register</a>
                        <a href="/api/user-login/" class="api-link">User Login</a>
                        <a href="/api/admin-login/" class="api-link">Admin Login</a>
                    </div>
                </div>

                <div class="card small-card">
                    <h2>Quiz APIs</h2>
                    <div class="link-grid">
                        <a href="/api/quizzes/" class="api-link">View Quizzes</a>
                        <a href="/api/quizzes/create/" class="api-link">Create Quiz</a>
                        <a href="/api/quizzes/1/update/" class="api-link">Update Quiz</a>
                        <a href="/api/quizzes/1/delete/" class="api-link">Delete Quiz</a>
                        <a href="/api/quiz-response/" class="api-link">Submit Response</a>
                        <a href="/api/quiz-feedback/10/" class="api-link">Get Feedback</a>
                    </div>
                </div>
            </div>

            <div class="col">
                <div class="card">
                    <h2>Blog APIs</h2>
                    <div class="link-grid">
                        <a href="/api/blogs/" class="api-link">View Blogs</a>
                        <a href="/api/blogs/create/" class="api-link">Create Blog</a>
                        <a href="/api/blogs/1/update/" class="api-link">Update Blog</a>
                        <a href="/api/blogs/1/delete/" class="api-link">Delete Blog</a>
                    </div>
                </div>

                <div class="card small-card">
                    <h2>Therapist APIs</h2>
                    <div class="link-grid">
                        <a href="/api/book-therapist/" class="api-link">Book Therapist</a>
                        <a href="/api/therapist-bookings/" class="api-link">View Bookings</a>
                    </div>
                </div>

                <div class="card small-card">
                    <h2>Trending APIs</h2>
                    <div class="link-grid">
                        <a href="/api/trending-search/" class="api-link">Trending Keywords</a>
                        <a href="/api/blogs-by-keyword/mental/" class="api-link">Blogs by Keyword</a>
                    </div>
                </div>
            </div>
        </div>
    </body>
    </html>
    """)
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status, permissions
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from rest_framework.permissions import IsAdminUser

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
def register_user(request):
    username = request.data.get('username')
    email = request.data.get('email')
    password = request.data.get('password')

    if User.objects.filter(username=username).exists():
        return Response({'error': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.create_user(username=username, email=email, password=password)
    user.save()

    return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)



@api_view(['GET'])
@permission_classes([IsAdminUser])  # Only admin can access
def list_users(request):
    users = User.objects.all().values('id', 'username', 'email', 'date_joined', 'is_active')
    return Response({'users': list(users)}, status=status.HTTP_200_OK)    

# --------------------------
# USER LOGIN
# --------------------------
@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def login_user(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)

    if user and user.is_active and not user.is_superuser:
        login(request, user)  # Set session
        return Response({
            'message': 'User login successful',
            'username': user.username,
            'uid': user.id
        }, status=status.HTTP_200_OK)
    return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

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