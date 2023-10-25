# Generated by Django 4.2.6 on 2023-10-24 10:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_user_email'),
        ('message', '0004_remove_chat_messages_chat_messages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='message_sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user'),
        ),
    ]
