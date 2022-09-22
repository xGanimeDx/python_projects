import os
from pytube import YouTube
from pytube.cli import on_progress

color = '\033[1;32;32m'
reset_color = '\033[39m'
path = os.path.dirname(os.path.abspath(__file__))

usr_input_url = input('Please enter valid YouTube video URL: ')
usr_input_res_value = ''
while usr_input_res_value not in ['360', '480', '720', '1080']:
    usr_input_res_value = input('Please choose the resolution (360, 480, 720, 1080): ')

def download_video(url: str, res_value: str) -> None:
    yt = YouTube(url, on_progress_callback=on_progress)
    print(yt.title)
    print('\n' + color + 'Downloading: ')
    yt.streams.filter(res=res_value + 'p', progressive=True).first().download(path)
    print('\nFinished downloading ' + reset_color)

download_video(usr_input_url, usr_input_res_value)
