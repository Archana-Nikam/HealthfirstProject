from django.urls import path
from .views import register_user, login_user, admin_login

urlpatterns = [
    path('api/register/', register_user, name='register_user'),
    path('api/login/', login_user, name='login_user'),
    path('api/admin-login/', admin_login, name='admin_login'),
]
