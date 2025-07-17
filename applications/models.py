# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from jobs.models import JobPost

class JobApplication(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('shortlisted', 'Shortlisted'),
        ('rejected', 'Rejected'),
        ('hired', 'Hired'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(JobPost, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    resume = models.FileField(upload_to='resumes/')
    cover_letter = models.TextField(blank=True)
    applied_at = models.DateTimeField(auto_now_add=True)
   
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')



    def __str__(self):
        return f"{self.full_name} applied for {self.job.title} status is {self.status}"
