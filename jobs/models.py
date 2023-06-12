# models.py

from django.db import models

from custom_model import BaseSoftDeletableModel




class Category(BaseSoftDeletableModel):
    
    title = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    created_by = models.IntegerField()

class JobApplication(models.Model):
    job_category = models.OneToOneField(Category, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    resume = models.FileField(upload_to='resumes/')
    cover_letter = models.TextField()

class JobDetail(models.Model):
    category = models.ForeignKey(Category, related_name='job_category', on_delete=models.CASCADE)
    job_title = models.CharField(max_length=255)
    job_detail = models.TextField()
    job_level = models.CharField(max_length=255)
    dateline = models.DateTimeField()
    posted_on = models.DateTimeField()

class Skill(models.Model):
    job_detail = models.ForeignKey(JobDetail, related_name='job_skills', on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=255)

class Responsibility(models.Model):
    job_detail = models.ForeignKey(JobDetail, related_name='job_responsibilities', on_delete=models.CASCADE)
    responsibility_name = models.CharField(max_length=255)

class Qualification(models.Model):
    job_detail = models.ForeignKey(JobDetail, related_name='job_qualifications', on_delete=models.CASCADE)
    qualification_name = models.CharField(max_length=255)
