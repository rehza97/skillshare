import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import *
from .forms import *
from django.db.models import Q , F

# Create your views here.


def chat(request, pk):
    url = request.META.get('HTTP_REFERER')
    
    # Assuming pk is the ID of the receiver
    form = ChatMessageForm()
    receiver = get_object_or_404(User, pk=pk)
    sender = request.user
    
    message_filter = Q(sender=request.user) | Q(receiver=request.user)
    myContact = Contact.objects.filter(message_filter)
    print(myContact)

# Create a Q object to represent the condition
    message_filter = Q(sender=request.user) | Q(receiver=request.user)

# Use the Q object in the query and apply distinct()
    myMsg = ChatMessage.objects.filter(message_filter).distinct()

    allshit = ChatMessage.objects.all()
    if request.method == 'POST':
        form = ChatMessageForm(request.POST)
        if form.is_valid():
            # Create an instance of the message
            message = form.save(commit=False)
            # Assign the sender to the current user
            message.sender = sender
            # Assign the receiver
            message.receiver = receiver
            message.seen = True
            # Save the message to the database
            message.save()
            return redirect(url)
            
    context = {
        'form': form,
        'myMsg': myMsg,
        'receiver': receiver,
        'sender': sender,
        'allshit': allshit,
        'myContact': myContact,
        
    }
    return render(request, 'chat/start_point_messages.html', context)


def sentMsg(request, pk):
    # Load the JSON data sent in the request body
    data = json.loads(request.body)
    rec = User.objects.get(id=pk)

# Check if a contact already exists between the users
    if Contact.objects.filter(sender=request.user, receiver=rec).exists():
        print('Contact already exists')
    else:
    # Create a new contact
        Contact.objects.create(sender=request.user, receiver=rec)
    # Extract the message from the JSON data
    new_chat = data['msg']
    
    # Get the sender's profile
    receiver = get_object_or_404(User, pk=pk)
    sender = request.user
    
    # Perform any further actions with the message data, such as saving it to the database
    print(f'''
          new_chat {new_chat}
          sender {sender}
          receiver {receiver}
          ''')    
    new_chat_msg = ChatMessage.objects.create(
        body = new_chat,
        sender = sender,
        receiver = receiver,
        seen = True
    )

    # Return a JsonResponse to confirm the message has been received
    return JsonResponse(
        {
            'message': f'{new_chat_msg.body}',
            'sender' : f'{new_chat_msg.sender}',
            # 'profile_pic':f'{new_chat_msg.msg_sender.pic}',
         }, status=200)

def recvMsg(request , pk):
    # data = json.loads(request.body)
    
    # Extract the message from the JSON data
    
    # Get the sender's profile
    receiver = get_object_or_404(User, pk=pk)
    sender = request.user
    chats = ChatMessage.objects.filter(sender = receiver , receiver=sender )
    arr = []
    for m in chats:
        arr.append(m.body)    
    return JsonResponse(arr,safe=False)
