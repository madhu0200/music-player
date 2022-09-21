import os.path

from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from .forms import *
# Create your views here.

def show(request):
    return render(request,'home.html')


#for uploading the music to the mysql server
def upload(request):
    if request.method=='POST':


        #song_obj = songs.objects.create(title=title,artist=artist,composer=composer,song=song)
       # song=songs(1,title,artist,composer,name)
        #song_obj.save()
        form=AudioForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'uploaded successfully')
        else:
            messages.success(request, 'error occured')
    return render(request,'upload.html')
song = songs.objects.all()
total = len(song)
# for listening the music
def listen(request):
    song=songs.objects.first()
    print(song)
    if song is not None:
        return render(request,'play.html',{'context':song,'total':total,'j':'1'})
    else:
        return HttpResponse("no songs to play")

from django.shortcuts import render

j=0

def next(request):

    global j
    j=j+1
    if j==len(song):
        j=0
    return render(request, 'play.html', {'context': song[j],'total':total,'j':j+1})


def previous(request):
    song=songs.objects.all()
    total = len(song)
    global j
    print(j)
    j=j-1
    if j<0:
        j=len(song)-1
    return render(request, 'play.html', {'context': song[j],'total':total,'j':j+1})

