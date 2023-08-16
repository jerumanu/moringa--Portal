from django.shortcuts import render

# Create your views here.
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from notifications.models import Notification

def create_notification(sender, recipient, message):
    notification = Notification.objects.create(
        recipient=recipient,
        message=message
    )
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        f"user_{recipient.id}", {"type": "notify", "notification": notification}
    )
