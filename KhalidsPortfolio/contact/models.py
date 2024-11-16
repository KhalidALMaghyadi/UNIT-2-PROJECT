from django.db import models

# Create your models here.
class ContactMessage(models.Model):
    name = models.CharField(max_length=1000)  # Full name of the sender
    email = models.EmailField()  # Email address of the sender
    subject = models.CharField(max_length=1000)  # Subject of the message
    message = models.TextField()  # The message content
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when the message was created