from django.shortcuts import render,get_object_or_404
from .models import JobPost
# Create your views here.
from django.shortcuts import render
from .models import JobPost
from applications.models import JobApplication

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



