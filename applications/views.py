from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import JobApplicationForm
from jobs.models import JobPost
from .models import JobApplication
from django.contrib import messages

@login_required
def apply_job(request, job_id):
    job = get_object_or_404(JobPost, id=job_id)

    # Prevent duplicate applications
    if JobApplication.objects.filter(user=request.user, job=job).exists():
        messages.warning(request, 'You have already applied for this job.')
        return redirect('home')

    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.user = request.user
            application.job = job
            application.save()
            messages.success(request, 'Application submitted successfully!')
            return redirect('home')
    else:
        form = JobApplicationForm()

    return render(request, 'applications/apply.html', {'form': form, 'job': job})


