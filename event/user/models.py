from django.db import models
from message.models import Message, Chat


class User(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    id = models.IntegerField(primary_key=True, max_length=10)
    email = models.EmailField(unique=True)
    unread_messages = models.ManyToManyField(Message, related_name='receivers', blank=True)
    chats = models.ManyToManyField(Chat, blank=True)


    def add_unread_message(self, message: Message) -> bool:
        """
        this function adds the ability 
        to add an unread message to a user.
        input: message of type Message -> Look in message.models
        returns bool       
        """
        if message.is_read:
            self.unread_messages.add(message)
            return True
        else: 
            return False
        
    
    def set_chat(self, chat: Chat) -> None:
        """
        this function sets a chat for a User
        and adds all the corresponding messages.
        input: chat of type Chat -> Look in message.models
        returns: None
        """
        self.chats.add(chat)
        for message in chat.messages.all():
            self.add_unread_message(message)