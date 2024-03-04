from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('video/<str:video_id>', views.video, name='home')
]