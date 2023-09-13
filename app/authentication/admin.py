from django.contrib import admin
from profiles.models import Educations, Experience, Profile
from jobs.models import Category, JobDetail, Qualification, Responsibility, Skill

from applications.models import JobApplication
from .models import User



# Register your models here.
admin.site.register(User)
admin.site.register(JobApplication)
admin.site.register(Category)
admin.site.register(JobDetail)
admin.site.register(Skill)
admin.site.register(Responsibility)
admin.site.register(Qualification)
admin.site.register(Profile)
admin.site.register(Educations)
admin.site.register(Experience)


