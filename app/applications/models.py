from django.db import models
from  authentication.models import User

from  jobs.models import Category

# Create your models here.

class JobApplication(models.Model):
    job_category = models.ForeignKey(Category, related_name='job_applications', on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    # resume = models.FileField(upload_to='resumes/')
    cover_letter = models.TextField()
    created_by = models.ManyToManyField(User)