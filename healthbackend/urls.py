from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import get_all_users 

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
    TokenBlacklistView,
)
from .views import register_user, admin_login, BlogViewSet

# Router for blog CRUD endpoints
router = DefaultRouter()
router.register(r'blogs', BlogViewSet, basename='blogs')

urlpatterns = [
    # Registration and authentication
    path('register/', register_user, name='register_user'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('token/blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),
    path('admin-login/', admin_login, name='admin_login'),

    # Blog API routes
    path('', include(router.urls)),  # /api/blogs/
    path('users/', get_all_users, name='get_all_users'),
]
