#Create by: Davy Pedro

from pytube import YouTube 
from pytube.cli import on_progress 
import os

operation = int(input('To download video, press (1) | To download audio, press (2): '))

if operation == 1:
    link = input('insert video link (YouTube only): ') 
    locale = input('Enter the location where the video will be saved: ')
    yt = YouTube(link, on_progress_callback = on_progress)

    print('Video title = ', yt.title)
    print('Audio size = ', yt.length, 'seconds')
    print('Download in progress...')

    #function to get the highest video resolution
    videos = yt.streams.get_highest_resolution()
    videos.download(locale)

    print('Download done successfully!')

else:
    link = input('insert audio link (YouTube only): ')
    locale = input('Enter the location where the video will be saved: ')
    yt = YouTube(link, on_progress_callback = on_progress)

    print('Audio title = ', yt.title)
    print('Audio size = ', yt.length, 'seconds')
    print('Download in progress...')

    videos = yt.streams.get_audio_only()
    out_file = videos.download(locale)

    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)

    print('Download done successfully!')


