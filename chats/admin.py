from django.contrib import admin
from .models import Chat, ChatMessage


@admin.register(Chat)
class ChatsAdmin(admin.ModelAdmin):
    list_display = ('freelancer', 'client')
    search_fields = ('freelancer__user__username', 'client__user__username')
    ordering = ('id',)


@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ('chat', 'message')
    search_fields = ('client', 'freelancer', 'chat.id')
