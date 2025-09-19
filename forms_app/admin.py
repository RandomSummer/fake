from django.contrib import admin
from .models import UserSubmission, Category, Feedback

@admin.register(UserSubmission)
class UserSubmissionAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'age', 'gender', 'created_at']
    list_filter = ['gender', 'newsletter', 'created_at']
    search_fields = ['first_name', 'last_name', 'email']
    readonly_fields = ['created_at', 'updated_at']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name']

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['user_submission', 'category', 'rating', 'created_at']
    list_filter = ['rating', 'category', 'created_at']
    search_fields = ['user_submission__email', 'comments']