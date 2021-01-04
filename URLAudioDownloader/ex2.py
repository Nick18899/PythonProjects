import requests
import os

REQUEST_STATUS_CODE = 200
name_dir = 'music_vk'
dir = input("Enter directory name ")
path = dir + name_dir
audio_id = input("Enter url ")
if not os.path.exists(path):
    os.makedirs(path)
os.chdir(path)
r = requests.get(audio_id)
if r.status_code == REQUEST_STATUS_CODE:
    with open("1" + '.mp3', 'wb') as output_file:
        output_file.write(r.content)