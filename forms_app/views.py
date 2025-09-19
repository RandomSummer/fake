from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from .models import UserSubmission, Feedback
from .forms import UserSubmissionForm, FeedbackForm

def submission_form(request):
    if request.method == 'POST':
        form = UserSubmissionForm(request.POST)
        if form.is_valid():
            submission = form.save()
            messages.success(request, 'Form submitted successfully!')
            return redirect('submission_success', pk=submission.pk)
    else:
        form = UserSubmissionForm()
    
    return render(request, 'forms_app/submission_form.html', {'form': form})

def submission_success(request, pk):
    submission = get_object_or_404(UserSubmission, pk=pk)
    return render(request, 'forms_app/submission_success.html', {'submission': submission})

def submission_list(request):
    query = request.GET.get('q')
    submissions = UserSubmission.objects.all()
    
    if query:
        submissions = submissions.filter(
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query) |
            Q(email__icontains=query)
        )
    
    paginator = Paginator(submissions, 10)  # 10 submissions per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'forms_app/submission_list.html', {
        'page_obj': page_obj,
        'query': query
    })

def feedback_form(request, submission_id):
    submission = get_object_or_404(UserSubmission, pk=submission_id)
    
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.user_submission = submission
            feedback.save()
            messages.success(request, 'Feedback submitted successfully!')
            return redirect('submission_list')
    else:
        form = FeedbackForm()
    
    return render(request, 'forms_app/feedback_form.html', {
        'form': form,
        'submission': submission
    })