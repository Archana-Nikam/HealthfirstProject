from django.urls import path
from .views import (
    register_user,
    login_user,
    login_admin,
    create_blog,
    list_blogs,
    get_blog,
    update_blog,
    delete_blog,
    list_quizzes,
    create_quiz,
    get_quiz,
    update_quiz,
    delete_quiz,
    submit_quiz_response,
    get_quiz_feedback_by_score,
    book_therapist,
    list_therapist_bookings,
    list_trending_keywords,
    blogs_by_trending_keyword,
    api_root_view  # ✅ Import the API root view
)

urlpatterns = [

    # -----------------------------
    # API Dashboard Root (HTML View)
    # -----------------------------
    path('', api_root_view, name='api-root'),  # ✅ Shows API landing page at /api/

    # -----------------------------
    # User & Admin Authentication
    # -----------------------------
    path('register/', register_user, name='register_user'),              # User Registration
    path('user-login/', login_user, name='login_user'),                  # User Login
    path('admin-login/', login_admin, name='login_admin'),              # Admin Login

    # -----------------------------
    # Blog CRUD Endpoints
    # -----------------------------
    path('blogs/', list_blogs, name='list_blogs'),
    path('blogs/create/', create_blog, name='create_blog'),
    path('blogs/<int:pk>/', get_blog, name='get_blog'),
    path('blogs/<int:pk>/update/', update_blog, name='update_blog'),
    path('blogs/<int:pk>/delete/', delete_blog, name='delete_blog'),

    # -----------------------------
    # Quiz & Question APIs
    # -----------------------------
    path('quizzes/', list_quizzes, name='quiz-list'),
    path('quizzes/create/', create_quiz, name='quiz-create'),
    path('quizzes/<int:pk>/', get_quiz, name='quiz-detail'),
    path('quizzes/<int:pk>/update/', update_quiz, name='quiz-update'),
    path('quizzes/<int:pk>/delete/', delete_quiz, name='quiz-delete'),
    path('quiz-response/', submit_quiz_response, name='quiz-response'),
    path('quiz-feedback/<int:score>/', get_quiz_feedback_by_score, name='quiz-feedback'),

    # -----------------------------
    # Therapist Booking APIs
    # -----------------------------
    path('book-therapist/', book_therapist, name='book_therapist'),
    path('therapist-bookings/', list_therapist_bookings, name='therapist_booking_list'),

    # -----------------------------
    # Trending Search APIs
    # -----------------------------
    path('trending-search/', list_trending_keywords, name='list-trending'),
    path('blogs-by-keyword/<str:keyword>/', blogs_by_trending_keyword, name='blogs-by-keyword'),
]
