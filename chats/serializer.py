from rest_framework import serializers
from chats.models import ChatMessage, Chat


class ChatMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatMessage
        fields = ['chat', 'sender', 'message']
