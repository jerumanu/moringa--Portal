# populate.py

import random
import string
import os
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.utils.crypto import get_random_string
from django.core.files import File
from django.conf import settings

from jobs.models import Category, JobApplication, JobDetail, Skill, Responsibility, Qualification

User = get_user_model()


class Command(BaseCommand):
    help = 'Populates the database with some testing data.'

    def add_arguments(self, parser):
        parser.add_argument('num_categories', type=int, default=5, help='Number of categories to create')
        parser.add_argument('num_jobs', type=int, default=10, help='Number of jobs to create')
        parser.add_argument('num_applications', type=int, default=50, help='Number of job applications to create')
        parser.add_argument('num_skills', type=int, default=3, help='Number of skills per job')
        parser.add_argument('num_responsibilities', type=int, default=5, help='Number of responsibilities per job')
        parser.add_argument('num_qualifications', type=int, default=3, help='Number of qualifications per job')
        parser.add_argument('num_users', type=int, default=5, help='Number of users to create')

    def handle(self, *args, **options):
        num_categories = options['num_categories']
        num_jobs = options['num_jobs']
        num_applications = options['num_applications']
        num_skills = options['num_skills']
        num_responsibilities = options['num_responsibilities']
        num_qualifications = options['num_qualifications']
        num_users = options['num_users']

        self.create_categories(num_categories)
        self.create_jobs(num_jobs, num_skills, num_responsibilities, num_qualifications)
        self.create_applications(num_applications)
        self.create_users(num_users)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database.'))

    def create_categories(self, num_categories):
        for _ in range(num_categories):
            category = Category.objects.create(
                title=get_random_string(10),
                position=get_random_string(10),
                location=get_random_string(10),
                created_by=random.randint(1, 3)
            )

    def create_jobs(self, num_jobs, num_skills, num_responsibilities, num_qualifications):
        categories = Category.objects.all()

        for _ in range(num_jobs):
            category = random.choice(categories)
            job_detail = JobDetail.objects.create(
                category=category,
                job_title=get_random_string(15),
                job_detail=get_random_string(50),
                job_level=get_random_string(10),
                dateline=get_random_datetime(),
                posted_on=get_random_datetime(),
            )

            self.create_skills(job_detail, num_skills)
            self.create_responsibilities(job_detail, num_responsibilities)
            self.create_qualifications(job_detail, num_qualifications)

    def create_skills(self, job_detail, num_skills):
        for _ in range(num_skills):
            skill = Skill.objects.create(
                job_detail=job_detail,
                skill_name=get_random_string(10)
            )

    def create_responsibilities(self, job_detail, num_responsibilities):
        for _ in range(num_responsibilities):
            responsibility = Responsibility.objects.create(
                job_detail=job_detail,
                responsibility_name=get_random_string(10)
            )

    def create_qualifications(self, job_detail, num_qualifications):
        for _ in range(num_qualifications):
            qualification = Qualification.objects.create(
                job_detail=job_detail,
                qualification_name=get_random_string(10)
        )