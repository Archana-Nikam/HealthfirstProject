from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
    TokenBlacklistView,
)
from .views import register_user, admin_login

urlpatterns = [
    # ✅ Custom registration
    path('api/register/', register_user, name='register_user'),

    # ✅ JWT login (returns access and refresh tokens)
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

    # ✅ JWT token refresh endpoint
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # ✅ JWT token verify endpoint (optional, good for security)
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    # ✅ Token blacklist (optional, for logout implementations)
    path('api/token/blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),

    # ✅ Custom admin-only login check (if needed)
    path('api/admin-login/', admin_login, name='admin_login'),
]
