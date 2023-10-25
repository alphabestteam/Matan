from django.db import models


class Message(models.Model):
    send_date = models.DateField()
    message_sender = models.ForeignKey(to='user.User', blank= False, on_delete=models.CASCADE, null=False)
    is_read = models.BooleanField(default=False)
    text = models.TextField(null=True)  
    chats = models.ForeignKey(to='message.Chat', related_name='messages', on_delete=models.CASCADE, null=True)
        

class Chat(models.Model):
    chat_id = models.AutoField(primary_key=True)  