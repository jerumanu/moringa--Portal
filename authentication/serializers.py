from jobs.models import Skill
from jobs.serializers import SkillSerializer
from .models import User, Profile
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.utils import timezone


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'email',
            'password',
            'first_name',
            'last_name',
            

        )

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
            password=validated_data ['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
            
        )
        user.set_password(validated_data['password'])
        user.save()
        return user




class UserLoginSerializer(serializers.Serializer):
    
    email = serializers.EmailField()
    password = serializers.CharField(max_length=128, write_only=True)
    access = serializers.CharField(read_only=True)
    refresh = serializers.CharField(read_only=True)
    role = serializers.CharField(read_only=True)

    def validate(self, data):
        email = data['email']
        password = data['password']
        user = authenticate(email=email, password=password)

        if user is None:
            raise serializers.ValidationError("Invalid login credentials")

        try:
            refresh = RefreshToken.for_user(user)
            refresh_token = str(refresh)
            access_token = str(refresh.access_token)

            user.last_login = timezone.now()
            user.save()

            validation = {
                'access': access_token,
                'refresh': refresh_token,
                'email': user.email,
                'role': user.role,
            }

            return validation
        except User.DoesNotExist:
            raise serializers.ValidationError("Invalid login credentials")
        
class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'email',
            'role'
        )

class ProfileSerializer(serializers.ModelSerializer):
    user = UserRegistrationSerializer()
    skills = SkillSerializer(many=True, read_only=True)

    class Meta:
        model = Profile
        fields = ('id', 'user', 'description', 'skills')

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user_serializer = UserRegistrationSerializer(data=user_data)
        user_serializer.is_valid(raise_exception=True)
        user = user_serializer.save()

        skills_data = validated_data.pop('skills')  # Assuming skills are passed as a list of dictionaries
        profile = Profile.objects.create(user=user, **validated_data)

        for skill_data in skills_data:
            Skill.objects.create(profile=profile, **skill_data)

        return profile
