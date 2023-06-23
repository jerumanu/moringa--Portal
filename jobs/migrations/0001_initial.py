# Generated by Django 4.1.7 on 2023-06-22 19:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False)),
                ('deleted_at', models.DateTimeField(default=None, null=True)),
                ('title', models.CharField(max_length=255)),
                ('position', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('created_by', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='JobDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=255)),
                ('job_detail', models.TextField()),
                ('job_level', models.CharField(max_length=255)),
                ('dateline', models.DateTimeField()),
                ('posted_on', models.DateTimeField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_details', to='jobs.category')),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(max_length=255)),
                ('job_detail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_skills', to='jobs.jobdetail')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile_skills', to='authentication.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Responsibility',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('responsibility_name', models.CharField(max_length=255)),
                ('job_detail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_responsibilities', to='jobs.jobdetail')),
            ],
        ),
        migrations.CreateModel(
            name='Qualification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qualification_name', models.CharField(max_length=255)),
                ('job_detail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_qualifications', to='jobs.jobdetail')),
            ],
        ),
        migrations.CreateModel(
            name='JobApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=20)),
                ('resume', models.FileField(upload_to='resumes/')),
                ('cover_letter', models.TextField()),
                ('job_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_applications', to='jobs.category')),
            ],
        ),
    ]
