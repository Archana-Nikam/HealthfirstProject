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
    list_quizzes,
    create_quiz,
    get_quiz,
    update_quiz,
    delete_quiz,
    submit_quiz_response,         
    get_quiz_feedback_by_score,
    book_therapist, 
    list_therapist_bookings   
       
       
         
)

urlpatterns = [
    # User and Admin Auth
    path('register/', register_user, name='register_user'),
    path('admin-login/', login_admin, name='admin_login'),

    # Blog API endpoints
    path('blogs/', list_blogs, name='list_blogs'),                  
    path('blogs/create/', create_blog, name='create_blog'),        
    path('blogs/<int:pk>/', get_blog, name='get_blog'),            
    path('blogs/<int:pk>/update/', update_blog, name='update_blog'),
    path('blogs/<int:pk>/delete/', delete_blog, name='delete_blog'),

    # Quiz CRUD endpoints
    path('quizzes/', list_quizzes, name='quiz-list'),
    path('quizzes/create/', create_quiz, name='quiz-create'),
    path('quizzes/<int:pk>/', get_quiz, name='quiz-detail'),
    path('quizzes/<int:pk>/update/', update_quiz, name='quiz-update'),
    path('quizzes/<int:pk>/delete/', delete_quiz, name='quiz-delete'),

    # Quiz Response Submission & Feedback
    path('quiz-response/', submit_quiz_response, name='quiz-response'),  # POST: submit quiz
    path('quiz-feedback/<int:score>/', get_quiz_feedback_by_score, name='quiz-feedback'),  # Optional: GET feedback from score only

    path('book-therapist/', book_therapist, name='book_therapist'),
    path('therapist-bookings/', list_therapist_bookings, name='therapist_booking_list'),
]
