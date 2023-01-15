"""
this module provides the record_sound function that records
an audio for 22s, modifies its PATH and provides 3 
wav files in the sounds folder
"""

import pyautogui
from time import sleep
from pathlib import Path
import os
from pydub import AudioSegment
from mutagen.mp3 import MP3

def record_sound():
    # opening apowerREC
    pyautogui.hotkey('win', 'd')
    pyautogui.hotkey('win')
    sleep(1)
    pyautogui.typewrite("ApowerREC")
    sleep(0.9)
    pyautogui.hotkey('enter')

    # recording the audio
    sleep(12)  # time it takes the recorder to open on my PC
    pyautogui.hotkey('f7')
    sleep(2)
    pyautogui.click(558, 512)  # this click may vary according to the pixel density that your PC has
    sleep(3.5 + 22)  # the 3s are the time that my recorder takes to start a
    #  recording the 22s is an estimated time from the hotmail questionnaire
    pyautogui.hotkey('f7')

    # closing the recorder
    os.system('taskkill /f /im ApowerREC.exe')

    oldAdress = 'D://ApowerREC/'  # modify where your files are saved
    newAdress = 'D://vscode/python/python-files/hotmail_generetor/funcaptcha/sounds/'  # modify where the project is saved on your PC

    # list in descending order the most recent files in the folder
    creation_date = lambda f: f.stat().st_ctime
    directory = Path(oldAdress)
    files = directory.glob('*.mp3')
    sorted_files = sorted(files, key=creation_date, reverse=True)
    # move folder file
    os.rename(f"{sorted_files[0]}", f"{newAdress}FullAudio.mp3")

    # taking the time of the audio
    audio = MP3('D://vscode/python/python-files/hotmail_generetor/funcaptcha/sounds/FullAudio.mp3')
    audio_time = int(audio.info.length)

    # cutting the mp3 audio and converting it to wav
    for i in range(3):
        if i == 0:
            os.system(f'ffmpeg -ss 0 -t {int(audio_time / 3)} -i {newAdress + "FullAudio.mp3"} {newAdress + str(i)}.mp3')
        else:
            os.system(f'ffmpeg -ss {int((audio_time / 3) * i)} -t {int((audio_time / 3) * (i + 1))} -i {newAdress + "FullAudio.mp3"} { newAdress + str(i)}.mp3')

    # converting mp3 to wav
        sleep(.6)
        audSeg = AudioSegment.from_mp3(newAdress + f'{i}.mp3')  
        audSeg.export(newAdress + f'{i}.wav', format="wav")  

        os.remove(f"{newAdress}{i}.mp3")  # removing mp3 files from folder
        os.system('cls')
    os.remove(newAdress + 'FullAudio.mp3')


if __name__ == "__main__":
    record_sound()
