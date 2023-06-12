

from rest_framework import serializers
from .models import Category, JobDetail, Skill, Responsibility, Qualification,JobApplication

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['skill_name']

class ResponsibilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Responsibility
        fields = ['responsibility_name']

class QualificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qualification
        fields = ['qualification_name']

class JobDetailSerializer(serializers.ModelSerializer):
    job_skills = SkillSerializer(many=True)
    job_responsibilities = ResponsibilitySerializer(many=True)
    job_qualifications = QualificationSerializer(many=True)

    class Meta:
        model = JobDetail
        fields = ['job_title', 'job_detail', 'job_level', 'dateline', 'posted_on', 'job_skills', 'job_responsibilities', 'job_qualifications']

class CategorySerializer(serializers.ModelSerializer):
    job_category = JobDetailSerializer(many=True)

    class Meta:
        model = Category
        fields = ['title', 'position', 'location', 'created_by', 'job_category']

    def create(self, validated_data):
        job_category_data = validated_data.pop('job_category')
        category = Category.objects.create(**validated_data)

        for job_data in job_category_data:

            job_skills_data = job_data.pop('job_skills')
            job_responsibilities_data = job_data.pop('job_responsibilities')
            job_qualifications_data = job_data.pop('job_qualifications')
            job_detail = JobDetail.objects.create(category=category, **job_data)

            for skill_data in job_skills_data:
                Skill.objects.create(job_detail=job_detail, **skill_data)
            for responsibility_data in job_responsibilities_data:
                Responsibility.objects.create(job_detail=job_detail, **responsibility_data)
            for qualification_data in job_qualifications_data:
                Qualification.objects.create(job_detail=job_detail, **qualification_data)
                
        return category




class JobApplicationSerializer(serializers.ModelSerializer):
    job_category=CategorySerializer()
    class Meta:
        model = JobApplication
        fields = ['id', 'full_name', 'email', 'phone_number', 'resume', 'cover_letter','job_category']

    def create(self, validated_data):
        job_category_data = validated_data.pop('job_category')
        job_category = Category.objects.create(**job_category_data)
        application = JobApplication.objects.create(job_application=job_category, **validated_data)
        return application


