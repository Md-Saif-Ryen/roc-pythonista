import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"    #To_run_pyg_when_not_running
from pygame import mixer
import time, datetime
from threading import Thread
import csv


class Healthy():


    def get_time(self):
        """Gives you the current local time
        in normal format with AM/PM."""
        current = datetime.datetime.now()
        in_format = current.strftime("%T %p")
        return in_format


    def get_date(self):
        """Gives you date in usual format."""
        current = datetime.datetime.now()
        in_format = current.strftime("%D")
        return in_format


    def pani_pilo(self):
        """For a given interval,it will remind the user to drink water,
        along with logging that data in a txt file."""

        i = 0
        while i < 1:
            time.sleep(self.timerw*60)
            mixer.init()
            mixer.music.load("water.mp3")  # https://www.zedge.net/ringtone/37a4492f-2da0-3cba-82c1-834466a24437
            mixer.music.play(5)
            while True:  # trick_to_play_sound_with_pyg
                mixer.music.unpause()
                print("Please enter 'w' to make sure you have taken a glass of water.")
                water = input()
                if water == "w":
                    mixer.music.stop()
                    with open(f"Healthy {self.name}.csv", "a") as health_data:
                        fieldnames = ["Date", "Time", "Water", "Eyes", "Exercise"]
                        csv_writer = csv.DictWriter(health_data, fieldnames=fieldnames, delimiter=",")

                        csv_writer.writeheader()
                        dict = {"Date": self.get_date(), "Time": self.get_time(), "Water":"Check", "Eyes": "N/A", "Exercise":"N/A"}
                        csv_writer.writerow(dict)
                    break
                else:
                    continue
            i += 1


    def protect_eyes(self):
        """For a given interval,it will remind the user to relax his/her eyes,
        along with logging that data in a txt file."""

        i = 0
        while i < 1:
            time.sleep(self.timere*60)
            mixer.init()
            mixer.music.load("eyes_of_you.mp3")  ##https://www.zedge.net/ringtone/69fc19dd-023f-4286-b173-b5107cece10f
            mixer.music.play(5)
            while True:
                mixer.music.unpause()
                print("Please enter 'e' to make sure you have relaxed your eyes for a moment.")
                water = input()
                if water == "e":
                    mixer.music.stop()
                    with open(f"Healthy {self.name}.csv", "a") as health_data:
                        fieldnames = ["Date", "Time", "Water", "Eyes", "Exercise"]
                        csv_writer = csv.DictWriter(health_data, fieldnames=fieldnames, delimiter=",")


                        dict = {"Date": self.get_date(), "Time": self.get_time(), "Water": "N/A", "Eyes": "Check",
                                "Exercise": "N/A"}
                        csv_writer.writerow(dict)
                    break
                else:
                    continue
            i += 1

    def physical_Ex(self):
        """For a given interval,it will remind the user to do some physical work,
         along with logging that data in a txt file."""

        i = 0
        while i < 1:
            time.sleep(self.timerp*60)
            mixer.init()
            mixer.music.load(
                "time_to_exercise.mp3")  ##https://www.zedge.net/ringtone/28be1f29-12eb-4355-8193-b19477128868
            mixer.music.play(5)
            while True:
                mixer.music.unpause()
                print("Please enter 'p' to make sure you have done a bit of physical movement.")
                water = input()
                if water == "p":
                    mixer.music.stop()
                    with open(f"Healthy {self.name}.csv", "a") as health_data:
                        fieldnames = ["Date", "Time", "Water", "Eyes", "Exercise"]
                        csv_writer = csv.DictWriter(health_data, fieldnames=fieldnames, delimiter=",")


                        dict = {"Date": self.get_date(), "Time": self.get_time(), "Water": "N/A", "Eyes": "N/A",
                                "Exercise": "Check"}
                        csv_writer.writerow(dict)
                    break
                else:
                    continue
            i += 1

    def execution(self):
        if __name__ == '__main__':
            print("Welcome.! I am your health manager.")
            time.sleep(1)
            self.name = input("Please enter your name here ---> ")
            time.sleep(1)
            print(f"{self.name},Let me manage your health.")
            time.sleep(1)
            print("You just focus on your work.!")
            time.sleep(1)
            while True:
                try:
                    self.timerw = float(input("Set your 'Water drinking Timer'(in minutes) here ---> "))
                    break
                except Exception as e:
                    print("Set in numbers.!")
                    continue

            while True:
                try:
                    self.timere = float(input("Set your 'Eyes relaxation Timer' here ---> "))
                    break
                except Exception as e:
                    print("Set in numbers.!")
                    continue

            while True:
                try:
                    self.timerp = float(input("Set your 'Body movement Timer' here ---> "))
                    break
                except Exception as e:
                    print("Set in number.!")
            print("Now,I will remind you at the time fixed.")
            time.sleep(1)
            print("Good Luck with your work.!")
            Thread(target=roc.pani_pilo).start()
            Thread(target=roc.protect_eyes).start()
            Thread(target=roc.physical_Ex).start()

roc = Healthy()
roc.execution()




















