

from rest_framework import serializers

from  applications.serializers import JobApplicationSerializer


from .models import Category, JobDetail, Skill, Responsibility, Qualification

class SkillSerializer(serializers.ModelSerializer):

    class Meta:
        model = Skill
        fields = ['id','skill_name']

class ResponsibilitySerializer(serializers.ModelSerializer):

    class Meta:
        
        model = Responsibility
        fields = ['id','responsibility_name']

class QualificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qualification
        fields = ['id','qualification_name']
class JobDetailSerializer(serializers.ModelSerializer):
    applications = JobApplicationSerializer(many=True, read_only=True)
    job_skills = SkillSerializer(many=True)
    job_responsibilities = ResponsibilitySerializer(many=True)
    job_qualifications = QualificationSerializer(many=True)

    class Meta:
        model = JobDetail
        fields = ['id','job_title', 'job_detail', 'job_level', 'dateline', 'posted_on', 'job_skills', 'job_responsibilities', 'job_qualifications','applications']

    def create(self, validated_data):
        job_skills_data = validated_data.pop('job_skills')
        job_responsibilities_data = validated_data.pop('job_responsibilities')
        job_qualifications_data = validated_data.pop('job_qualifications')

        job_detail = JobDetail.objects.create(**validated_data)

        skills = [Skill(job_detail=job_detail, **skill_data) for skill_data in job_skills_data]
        responsibilities = [Responsibility(job_detail=job_detail, **responsibility_data) for responsibility_data in job_responsibilities_data]
        qualifications = [Qualification(job_detail=job_detail, **qualification_data) for qualification_data in job_qualifications_data]

        Skill.objects.bulk_create(skills)
        Responsibility.objects.bulk_create(responsibilities)
        Qualification.objects.bulk_create(qualifications)

        return job_detail


class CategorySerializer(serializers.ModelSerializer):
    job_details = JobDetailSerializer(many=True)

    class Meta:
        model = Category
        fields =  '__all__'

    def create(self, validated_data):
        job_category_data = validated_data.pop('job_details')
        category = Category.objects.create(**validated_data)

        job_details = []
        skills = []
        responsibilities = []
        qualifications = []

        for job_data in job_category_data:
            job_skills_data = job_data.pop('job_skills')
            job_responsibilities_data = job_data.pop('job_responsibilities')
            job_qualifications_data = job_data.pop('job_qualifications')

            job_detail = JobDetail(category=category, **job_data)
            job_details.append(job_detail)

            skills.extend([Skill(job_detail=job_detail, **skill_data) for skill_data in job_skills_data])
            responsibilities.extend([Responsibility(job_detail=job_detail, **responsibility_data) for responsibility_data in job_responsibilities_data])
            qualifications.extend([Qualification(job_detail=job_detail, **qualification_data) for qualification_data in job_qualifications_data])

        JobDetail.objects.bulk_create(job_details)
        Skill.objects.bulk_create(skills)
        Responsibility.objects.bulk_create(responsibilities)
        Qualification.objects.bulk_create(qualifications)

        return category
