# healthbackend/urls.py
from django.urls import path
from . import views
from .views import (
    register_user,
    login_admin,
    create_blog,
    list_blogs,
    get_blog,
    update_blog,
    delete_blog,
)

urlpatterns = [
    path('register/', register_user, name='register_user'),
    path('admin-login/', login_admin, name='admin_login'),

    # Blog API endpoints (Function-Based Views)
    path('blogs/', list_blogs, name='list_blogs'),                  # GET all blogs
    path('blogs/create/', create_blog, name='create_blog'),        # POST new blog
    path('blogs/<int:pk>/', get_blog, name='get_blog'),            # GET one blog
    path('blogs/<int:pk>/update/', update_blog, name='update_blog'),  # PUT update
    path('blogs/<int:pk>/delete/', delete_blog, name='delete_blog'),  # DELETE blog



    path('quizzes/', views.list_quizzes, name='quiz-list'),
    path('quizzes/create/', views.create_quiz, name='quiz-create'),
    path('quizzes/<int:pk>/', views.get_quiz, name='quiz-detail'),
    path('quizzes/<int:pk>/update/', views.update_quiz, name='quiz-update'),
    path('quizzes/<int:pk>/delete/', views.delete_quiz, name='quiz-delete'),
]
