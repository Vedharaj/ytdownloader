from django.shortcuts import render
from django.http import JsonResponse
from pytube import YouTube

# Create your views here.
def home(req):
    return JsonResponse({"status": "success", "msg": "app working well!"})

def video(req, video_id):
    video_url = "https://youtu.be/"+video_id
    yt = YouTube(video_url)
    duration_in_seconds = yt.length

    duration_formatted = str(int(duration_in_seconds // 3600)).zfill(2) + ":" + \
                             str(int((duration_in_seconds % 3600) // 60)).zfill(2) + ":" + \
                             str(int(duration_in_seconds % 60)).zfill(2)
    if duration_formatted[0:2] == "00":
        duration_formatted = duration_formatted[3:]
    return JsonResponse({"status": "success", "data":{'title': yt.title, 'author': yt.author, 'duration': duration_formatted}})