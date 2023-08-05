from django.db import models
from users.models import Client, Freelancer, CustomUser


class Chat(models.Model):
    freelancer = models.ForeignKey(Freelancer, on_delete=models.CASCADE, related_name="chats_as_user1")
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="chats_as_user2")

    def __str__(self):
        return f'{self.freelancer.user.username} with {self.client.user.username}'

    class Meta:
        verbose_name = "Chat"
        verbose_name_plural = "Chats"


class ChatMessage(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        verbose_name = "ChatMessage"
        verbose_name_plural = "ChatMessages"
