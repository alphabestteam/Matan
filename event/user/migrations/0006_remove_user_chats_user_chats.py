# Generated by Django 4.2.6 on 2023-10-25 07:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0008_remove_chat_messages_alter_message_chats'),
        ('user', '0005_remove_user_chats_user_chats'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='chats',
        ),
        migrations.AddField(
            model_name='user',
            name='chats',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='message.chat'),
        ),
    ]
