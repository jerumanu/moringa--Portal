from django.db import models
from django.utils import timezone

from authentication.models import User

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_add_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True
        

class BaseSoftDeletableModel(models.Model):
    is_deleted = models.Boolean(default=False)
    deleted_at = models.DateTimeField(null=True)
    deleted_by = models.ForeignKey(User, null=True)
    
    class Meta:
        abstract = True
        
    def soft_delete(self, user_id=None):
        self.is_deleted = True
        self.deleted_by = user_id
        self.deleted_at = timezone.now()
        self.save()