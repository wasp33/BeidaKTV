from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from .models import Song, Singer
# Create your views here.

def hello_world(request,name):
    return render(request, 'hello_world.html', {
        'current_time': str(datetime.now()),
        'name': name,
    })
    #return HttpResponse("Hello World!")

def singers_show(request):
    singer_list = Singer.objects.all()
    return render(request, 'singers.html',{
        'singer_list': singer_list,
    })

def songs_show(request):
    song_list = Song.objects.all()
    return render(request, 'songs.html',{
        'song_list': song_list,
    })

def songs_show(request,singer):
    singer = Singer.objects.get(name=singer)
    song_list = Song.objects.filter(singer=singer.id)
    return render(request, 'songs.html',{
        'song_list': song_list,
    })

