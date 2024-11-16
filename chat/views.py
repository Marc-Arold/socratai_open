from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from Agents.main import activate_agents
from .models import Message, Rating, Conversation
import json


def renderchat(request):
    return render(request, 'Chat/chat.html')




def feedback(request):
   feedback = request.POST.get('feedback')
   write_feedback = Rating.objects.create(feedback=feedback)
   write_feedback.save()
   return redirect('chat:chat')
 


def conversation(request):
    if request.method == 'POST':
        # Check if there is form data
        user_message = request.POST.get('user_message')  # Get the message from form data
        
        if not user_message:
            return JsonResponse({'error': 'Le message utilisateur est manquant'}, status=400)
        
        try:
            # You can now process the message
            response_text = activate_agents(user_message)
              # Process the message using the agent
            chat_to_save = Message(user_message=user_message, bot_response=response_text)
            chat_to_save.save()
            return JsonResponse({'response_text': response_text})

        except Exception as e:
            return JsonResponse({'error': f'Une erreur est survenue: {str(e)}'}, status=500)