from django.http import JsonResponse, FileResponse
from pytube import YouTube
import io

from . import utilities

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

    video_streams = yt.streams.filter(type='video').all()

    resolutions = list(set([stream.resolution for stream in video_streams if stream.resolution]))

    return JsonResponse({
        "status": "success", 
        "data":{
            'title': yt.title,
            'author': yt.author,
            'duration': duration_formatted, 
            'streams': {
                'file_extension': ['mp4', 'webm'],
                'res': resolutions
            }
        }
    })

def video_downl(req, video_id):
    video_url = "https://youtu.be/"+video_id
    res = req.GET.get('res')
    file_extension = req.GET.get('fe')

    try:
        # yt = YouTube(video_url)

        # video_stream = yt.streams.filter(file_extension=file_extension, res=res).first()

        # video_stream.download()
        return FileResponse(open(YouTube(video_url).streams.filter(file_extension=file_extension, res=res).first().download(skip_existing=True), 'rb'), as_attachment=True)
    except:
        return JsonResponse({"status": "fail", "msg": "failed to download"})