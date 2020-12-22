import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"    #To_run_pyg_when_not_running
from pygame import mixer
import time, datetime
from threading import Thread
import csv


def get_time():
    """Gives you the current local time
    in normal format with AM/PM."""
    current = datetime.datetime.now()
    in_format = current.strftime("%T %p")
    return in_format
def get_date():
    """Gives you current date in usual format."""
    current = datetime.datetime.now()
    in_format = current.strftime("%D")
    return f"Date : {in_format}"


def pani_pilo():
    """For a given interval,it will remind the user to drink water,
    along with logging that data in a txt file."""
    file = open("My_Health.txt", "a")
    file.write("---------------" + get_date() + "---------------\n")
    i = 0
    while i < 1:
        time.sleep(5)
        mixer.init()
        mixer.music.load("water.mp3")  #https://www.zedge.net/ringtone/37a4492f-2da0-3cba-82c1-834466a24437
        mixer.music.play(5)
        while True:                  #trick_to_play_sound_with_pyg
            mixer.music.unpause()
            print("Please enter 'w' to make sure you have taken a glass of water.")
            water = input()
            if water == "w":
                mixer.music.stop()
                file = open("My_Health.txt", "a")
                file.write("[" + str(get_time()) + "]" + " : " + "Drank_wtr" + "\n")
                file.close()
                break
            else:
                continue
        i += 1

def prtct_eye():
    """For a given interval,it will remind the user to relax his/her eyes,
        along with logging that data in a txt file."""
    i = 0
    while i < 1:
        time.sleep(10)
        mixer.init()
        mixer.music.load("eyes_of_you.mp3")  ##https://www.zedge.net/ringtone/69fc19dd-023f-4286-b173-b5107cece10f
        mixer.music.play(5)
        while True:
            mixer.music.unpause()
            print("Please enter 'e' to make sure you have relaxed your eyes for a moment.")
            water = input()
            if water == "e":
                mixer.music.stop()
                file = open("My_Health.txt", "a")
                file.write("[" + str(get_time()) + "]" + " : " + "Eyes_sthd" + "\n")
                file.close()
                break
            else:
                continue
        i += 1

def phy_Ex():
    """For a given interval,it will remind the user to do some physical work,
        along with logging that data in a txt file."""
    i = 0
    while i < 1:
        time.sleep(15)
        mixer.init()
        mixer.music.load("time_to_exercise.mp3")  ##https://www.zedge.net/ringtone/28be1f29-12eb-4355-8193-b19477128868
        mixer.music.play(5)
        while True:
            mixer.music.unpause()
            print("Please enter 'p' to make sure you have done a bit of physical movement.")
            water = input()
            if water == "p":
                mixer.music.stop()
                file = open("My_Health.txt", "a")
                file.write("[" + str(get_time()) + "]" + " : " + "Body_rlxd" + "\n")
                file.close()
                break
            else:
                continue
        i += 1

###It helps in multiple funcitons at onces using Threading...
if __name__ == '__main__':
    Thread(target=pani_pilo).start()
    Thread(target=prtct_eye).start()
    Thread(target=phy_Ex).start()