from django.shortcuts import render, reverse, redirect
from users.models import Client, Freelancer
from .forms import MessageForm
from .models import Chat, ChatMessage
from django.http import JsonResponse, HttpResponseRedirect
from django.utils.timezone import now


def ChatsDetailView(request, chats_id):
    chat_obj = Chat.objects.get(id=chats_id)
    if request.user.user_type == 'client':
        user = Client.objects.get(user__id=request.user.id)
        chats = Chat.objects.filter(client__user__id=request.user.id).distinct('freelancer')
        recipient = chat_obj.freelancer

    else:
        user = Freelancer.objects.get(id=request.user.id)
        chats = Chat.objects.filter(freelancer__id=request.user.id).distinct('client')
        recipient = chat_obj.client.user
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data['message']
            ChatMessage.objects.create(message=message, chat=chat_obj, sender=request.user)

    elif request.method == 'GET':
        form = MessageForm()

    messages = reversed(ChatMessage.objects.filter(chat__id=chats_id))

    context = {
        'user': user,
        'recipient': recipient,
        'chats': chats,
        'messages': messages,
        'chats_id': chats_id,
        'form': form,
    }

    return render(request, 'chats/index.html', context=context)


def ChatsView(request):
    if request.user.user_type == 'client':
        print(request.user.id)
        user = Client.objects.get(user__id=request.user.id)
        chats = Chat.objects.filter(client__user__id=request.user.id)

    else:
        user = Freelancer.objects.get(user__id=request.user.id)
        chats = Chat.objects.filter(freelancer__id=request.user.id)

    context = {
        'user': user,
        'chats': chats,

        # 'chat_message': chat_message,
    }

    return render(request, 'chats/base.html', context)


def MessageRemove(request, message_id):
    message = ChatMessage.objects.get(id=message_id)
    message.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
