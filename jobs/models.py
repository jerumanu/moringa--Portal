# models.py
from django.db import models
from  profiles.models import Profile

from authentication.models import  User
from .custom_model import SoftDeleteModel

class Category(SoftDeleteModel):
    title = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)



class JobDetail(models.Model):
    category = models.ForeignKey(Category, related_name='job_details', on_delete=models.CASCADE)
    job_title = models.CharField(max_length=255)
    job_detail = models.TextField()
    job_level = models.CharField(max_length=255)
    dateline = models.DateTimeField()
    posted_on = models.DateTimeField()

class Skill(models.Model):
    job_detail = models.ForeignKey(JobDetail, related_name='job_skills', on_delete=models.CASCADE ,null=True)

    skill_name = models.CharField(max_length=255)
    profile = models.ForeignKey(Profile, related_name='profile_skills', on_delete=models.CASCADE, null=True)

class Responsibility(models.Model):
    job_detail = models.ForeignKey(JobDetail, related_name='job_responsibilities', on_delete=models.CASCADE)
    responsibility_name = models.CharField(max_length=255)

class Qualification(models.Model):
    job_detail = models.ForeignKey(JobDetail, related_name='job_qualifications', on_delete=models.CASCADE)
    qualification_name = models.CharField(max_length=255)
