

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
    applications =JobApplicationSerializer(many=True ,read_only=True)
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

        for skill_data in job_skills_data:
            Skill.objects.create(job_detail=job_detail, **skill_data)
        for responsibility_data in job_responsibilities_data:
            Responsibility.objects.create(job_detail=job_detail, **responsibility_data)
        for qualification_data in job_qualifications_data:
            Qualification.objects.create(job_detail=job_detail, **qualification_data)

        return job_detail
class CategorySerializer(serializers.ModelSerializer):
    job_details = JobDetailSerializer(many=True)
    # created_by = serializers.IntegerField(source='created_by.id', read_only=True)

    class Meta:
        model = Category
        fields = '__all__'

    def create(self, validated_data):
        job_category_data = validated_data.pop('job_details')
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

# class CategorySerializer(serializers.ModelSerializer):

#     job_details = JobDetailSerializer(many=True)
#     created_by = serializers.IntegerField(source='created_by.id', read_only=True)

#     class Meta:
#         model = Category
        
#         fields= '__all__'
#         # fields = ['id', 'title', 'position', 'location',  'job_details']
#         # extra_kwargs = {
#         #     'created_by': {'write_only': True}
#         # }
#     def create(self, validated_data):
#         job_category_data = validated_data.pop('job_details')
#         category = Category.objects.create(**validated_data)

#         for job_data in job_category_data:

#             job_skills_data = job_data.pop('job_skills')
#             job_responsibilities_data = job_data.pop('job_responsibilities')
#             job_qualifications_data = job_data.pop('job_qualifications')
#             job_detail = JobDetail.objects.create(category=category, **job_data)

#             for skill_data in job_skills_data:
#                 Skill.objects.create(job_detail=job_detail, **skill_data)
#             for responsibility_data in job_responsibilities_data:
#                 Responsibility.objects.create(job_detail=job_detail, **responsibility_data)
#             for qualification_data in job_qualifications_data:
#                 Qualification.objects.create(job_detail=job_detail, **qualification_data)
                
#         return category
    




