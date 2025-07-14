from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status, permissions, viewsets
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import UserProfileSerializer, BlogSerializer
from .models import Blog

# ✅ Register User View with JWT Token
@api_view(['POST'])
def register_user(request):
    serializer = UserProfileSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        return Response({
            'message': 'You have registered successfully!',
            'user': serializer.data,
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ✅ Login View
@api_view(['POST'])
def login_user(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)

    if user is not None:
        return Response({
            'message': 'Login successful!',
            'username': user.username,
            'uid': user.id,
            'is_admin': user.is_superuser
        }, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

# ✅ Admin Login View
@api_view(['POST'])
def admin_login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)

    if user is not None and user.is_superuser:
        return Response({
            'message': 'Admin login successful!',
            'username': user.username,
            'uid': user.id,
            'is_admin': user.is_superuser
        }, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Invalid admin credentials'}, status=status.HTTP_400_BAD_REQUEST)

# ✅ Blog CRUD ViewSet (Create, Read, Update, Delete)
class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all().order_by('-created_at')
    serializer_class = BlogSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
