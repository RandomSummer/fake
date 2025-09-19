from django.urls import path
from . import views

urlpatterns = [
    path('', views.submission_form, name='submission_form'),
    path('success/<int:pk>/', views.submission_success, name='submission_success'),
    path('list/', views.submission_list, name='submission_list'),
    path('feedback/<int:submission_id>/', views.feedback_form, name='feedback_form'),
]