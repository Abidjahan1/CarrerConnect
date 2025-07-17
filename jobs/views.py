from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import JobPost
# Create your views here.
from django.shortcuts import render
from .models import JobPost
from applications.models import JobApplication
from django.db.models import Count

def job_list(request):
    jobs = JobPost.objects.filter(is_active=True).order_by('-created_at')
    for job in jobs:
        job.app_count = JobApplication.objects.filter(job=job).count()
    return render(request, 'jobs/job_list.html', {'jobs': jobs})


def job_detail(request, job_id):
    job = get_object_or_404(JobPost, id=job_id)
    applicant_count = JobApplication.objects.filter(job=job).count()
    return render(request, 'jobs/job_detail.html', {
        'job': job,
        'applicant_count': applicant_count,
    })

@login_required
def applicant_dashboard(request):
    applications = JobApplication.objects.filter(user=request.user).order_by('-applied_at')

    # Count total applications
    total_applications = applications.count()

    # Count by status
    status_counts = applications.values('status').annotate(count=Count('status'))

    # Build dictionary like {'pending': 3, 'rejected': 1, ...}
    status_summary = {s['status']: s['count'] for s in status_counts}

    return render(request, 'jobs/applicant_dashboard.html', {
        'applications': applications[:5],  # show recent 5
        'total_applications': total_applications,
        'status_summary': status_summary
    })


