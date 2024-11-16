from django.shortcuts import render, redirect
from django.http import HttpRequest
from .models import ContactMessage
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.


def contact_view(request : HttpRequest):
    if request.method == "POST":
        new_data = ContactMessage(
          name = request.POST["name"],
          email = request.POST["email"],
          subject = request.POST["subject"], 
          message = request. POST["message"],  
     )
        new_data.save()
        name = new_data.name
        email = new_data.email
        message = new_data.message
        
        send_mail(
            f'New Contact Message from {name}',  
            f'You have received a new message from {name} ({email}):\n\n{message}',  
            'testproject.ta@gmail.com',  
            ['testproject.ta@gmail.com'],  
            fail_silently=False,
        )
        messages.success(request, "Your message has been sent successfully!")
        return redirect('contact:contact_view')
    
    return render(request, 'contact/contact_form.html')


def all_messages_view(request : HttpRequest):
    
    messages = ContactMessage.objects.all()

    return render(request, 'contact/all_messages.html', {'messages': messages})

def delete_message_view(request:HttpRequest,message_id):
    
    if request.method == 'POST':        
            message = ContactMessage.objects.get(pk=message_id)
            message.delete()
            
            return redirect('contact:all_messages_view')
    
         