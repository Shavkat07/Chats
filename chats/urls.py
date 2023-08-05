from django.urls import path
from .views import ChatsView, ChatsDetailView, MessageRemove

app_name = 'chats'

urlpatterns = [
    path('', ChatsView, name='chats'),
    path('chat/<int:chats_id>/', ChatsDetailView, name='chat_detail'),
    path('chat/<int:message_id>', MessageRemove, name='message_remove'),
]
