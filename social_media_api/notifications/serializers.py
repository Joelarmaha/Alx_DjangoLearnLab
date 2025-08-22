from rest_framework import serializers
from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    actor_username = serializers.ReadOnlyField(source="actor.username")
    recipient_username = serializers.ReadOnlyField(source="recipient.username")

    class Meta:
        model = Notification
        fields = ["id", "recipient_username", "actor_username", "verb", "timestamp", "read"]

