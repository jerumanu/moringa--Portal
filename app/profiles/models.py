from django.db import models

from  authentication.models import User

# Create your models here.



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description=models.CharField(max_length=250)
    # pic = models.ImageField()
    about=models.CharField(max_length=255)
    location=models.CharField(max_length=100)
    headline=models.CharField(max_length=100)
    current_position=models.CharField(max_length=100)



class Educations(models.Model):
    institution = models.CharField(max_length=255)
    professional = models.TextField()
    field_study = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    profile = models.ForeignKey(Profile, related_name='educations', on_delete=models.CASCADE)


class Experience(models.Model):
    title= models.CharField(max_length=255)
    employment_type = models.TextField()
    work_type = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    profile = models.ForeignKey(Profile, related_name='experiences', on_delete=models.CASCADE)

