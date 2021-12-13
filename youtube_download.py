#Create by: Davy Pedro

from pytube import YouTube 
'''
first install the pytube package. 
to install, just type "pip install pytube" in cmd as administrator'''

#library responsible for showing the progress of a given task on the terminal
from pytube.cli import on_progress 
import os

#variable to select download option
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
    videos.download(locale) #passing location to download function

    print('Download done successfully!')

else:
    link = input('insert audio link (YouTube only): ')
    locale = input('Enter the location where the video will be saved: ')
    yt = YouTube(link, on_progress_callback = on_progress)

    print('Audio title = ', yt.title)
    print('Audio size = ', yt.length, 'seconds')
    print('Download in progress...')

    '''
    different from the first case, where we select the highest resolution, 
    select the get_audio_only() function to get only the audio from the video. 
    However, the video screen is black. We need to deal with this.'''
    videos = yt.streams.get_audio_only()
    out_file = videos.download(locale)

    base, ext = os.path.splitext(out_file) #renaming and changing file extension to mp3
    new_file = base + '.mp3'
    os.rename(out_file, new_file)

    print('Download done successfully!')


