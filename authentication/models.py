import uuid

from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils import timezone


from .manager import CustomUserManager

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):

    # These fields tie to the roles!
    ADMIN = 1
    USER = 2
    

    ROLE_CHOICES = (
        (ADMIN, 'Admin'),
        (USER, 'User'),
        
    )
    
    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        

    uid = models.UUIDField(unique=True, editable=False, default=uuid.uuid4, verbose_name='Public identifier')
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True, default=2)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(default=timezone.now)
    created_by = models.EmailField()
    modified_by = models.EmailField()
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    # def type_to_string(self):
    #     if self.type == 'UN':
    #         return 'Unspecified'
    #     elif self.type == 'TU':
    #         return 'Tutorial'
    #     elif self.type == 'RS':
    #         return 'Research'
    #     elif self.type == 'RW':
    #         return 'Review'
        
    def __str__(self):
        return self.email
    


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description=models.CharField(max_length=250)

    def __str__(self):
        return self.user.email
