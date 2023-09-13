# from django.db import models

# from  authentication.models import User

# # models.py

# class Notification(models.Model):
#     user_revoker = models.ForeignKey(
#         User,
#         related_name='notifications_revoked',
#         on_delete=models.CASCADE
#     )
    
#     user_sender = models.ForeignKey(
#         User,
#         related_name='notifications_sent',
#         on_delete=models.CASCADE
#     )
    
#     status = models.CharField(max_length=264, null=True, blank=True, default="unread")
#     type_of_notification = models.CharField(max_length=264, null=True, blank=True)
