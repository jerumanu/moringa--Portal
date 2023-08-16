from rest_framework import serializers

from  applications.models import JobApplication
# from  jobs.serializers import CategorySerializer


class JobApplicationSerializer(serializers.ModelSerializer):
    
    # job_category = CategorySerializer(many=True, read_only=True)


    class Meta:
        model = JobApplication
        fields = '__all__'

    # def create(self, validated_data):
    #     job_category_data = validated_data.pop('job_category')
    #     job_category_serializer = CategorySerializer(data=job_category_data)
    #     job_category_serializer.is_valid(raise_exception=True)
    #     job_category = job_category_serializer.save()
        
    #     validated_data['job_category'] = job_category
    #     job_application = JobApplication.objects.create(**validated_data)
        
    #     return job_application
