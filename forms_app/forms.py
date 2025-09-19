from django import forms
from .models import UserSubmission, Feedback, Category

class UserSubmissionForm(forms.ModelForm):
    class Meta:
        model = UserSubmission
        fields = '__all__'
        exclude = ['created_at', 'updated_at']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+1234567890'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 120}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Your message...'}),
            'newsletter': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
    
    def clean_age(self):
        age = self.cleaned_data['age']
        if age < 1 or age > 120:
            raise forms.ValidationError("Age must be between 1 and 120")
        return age

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['category', 'rating', 'comments']
        widgets = {
            'category': forms.Select(attrs={'class': 'form-control'}),
            'rating': forms.Select(attrs={'class': 'form-control'}),
            'comments': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }