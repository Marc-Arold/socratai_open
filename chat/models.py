
from ast import mod
from django.db import models


# Create your models here.



class Conversation(models.Model):
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True, blank=True)
    description = models.CharField(max_length=255, blank=True, editable=False)
    active = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.description} - Started on {self.start_time.strftime('%Y-%m-%d %H:%M:%S')} "

class Message(models.Model):
    conversation = models.ForeignKey(Conversation, null=True,on_delete=models.CASCADE, related_name='messages')
    user_message = models.TextField(blank=True, null=True)  # Autorise NULL en base de données
    bot_response = models.TextField(blank=True, null=True)  # Autorise NULL en base de données
    timestamp = models.DateTimeField(auto_now_add=True)

class Rating(models.Model):
    feedback = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True) 