from multiprocessing.sharedctypes import Value
from django.shortcuts import render, redirect
from chat.models import Room, Message
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def room(request, room):
    username = request.GET.get('username')
    room_details = Room.objects.get(name = room)
    return render(request, 'room.html', {
        'username': username,
        'room': room,
        'room_details': room_details
    })

def checkview(request):
    room = request.POST['RoomCode']
    username = request.POST['Username']

    if Room.objects.filter(name = room).exists():
        return redirect('/'+ room + '/?username=' + username)
    else:
        new_room = Room.objects.create(name = room)
        new_room.save()
        return redirect('/'+ room + '/?username=' + username)

def send(request):
    content = request.POST['content']
    room_id = request.POST['room_id']
    username = request.POST['username']

    new_message = Message.objects.create(content = content, user = username, room = room_id)
    new_message.save()
    return HttpResponse('Message Sent !')
