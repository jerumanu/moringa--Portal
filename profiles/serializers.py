from rest_framework import serializers
from jobs.models import Skill
from jobs.serializers import SkillSerializer

from profiles.models import Educations, Experience, Profile

class EducationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Educations
        fields =['id','institution','professional','field_study','start_date','end_date'] 

class ExperienceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Experience
        fields =['id','title','employment_type','work_type','description','start_date','end_date']


class ProfileSerializer(serializers.ModelSerializer):
    
    profile_skills = SkillSerializer(many=True)
    educations = EducationSerializer(many=True)
    experiences = ExperienceSerializer(many=True)

    class Meta:
        model = Profile
        fields = '__all__'


    def create(self, validated_data):
        profile_skills_data = validated_data.pop('profile_skills')
        educations_data = validated_data.pop('educations')
        experiences_data = validated_data.pop('experiences')

        profile = Profile.objects.create(**validated_data)

        for skill_data in profile_skills_data:
            Skill.objects.create(profile=profile, **skill_data)
        for education_data in educations_data:
            Educations.objects.create(profile=profile, **education_data)
        for experience_data in experiences_data:
            Experience.objects.create(profile=profile, **experience_data)

        return profile