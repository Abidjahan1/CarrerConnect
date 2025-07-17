from django.utils import timezone
from django.db import models

# Create your models here.
class JobPost(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=100)
    qualifications = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    deadline = models.DateField()

    def __str__(self):
        return self.title
    
    def is_expired(self):
        return self.deadline < timezone.now().date()