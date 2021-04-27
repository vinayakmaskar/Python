import time
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
from pygame import mixer
import datetime


def music(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play(-1)

    while True:
        a = input("Enter stop to end the alarm: ")

        if a != stopper:
            print("Invalid entry!")
            continue
        else:
            if a == stopper:
                mixer.music.stop()
                print("Alarm has been stopped!")
                break



def user():
    global hour, min
    global ampm

    print("\nEnter the following for setting the alarm!")
    print("Enter in HH:MM AM/PM format")

    try:
        hour = int(input("Enter hour: "))
        if hour > 12:
            print("Hour should not be greater than 12!")
            return user()
        min = int(input("Enter minutes: "))

        if min > 59:
            print("Minute should not be greater than 59!")
            return user()

    except Exception as error:
        print("Please enter integer!")
        return user()



    ap = int(input("1.AM\n2.PM\nEnter 1 or 2: "))
    if ap == 1:
        ampm = "AM"
    else:
        ampm = "PM"
    print(f"Alarm has been set for {hour}:{min} {ampm}")

user()




def alarm():
    while True:
        global re
        global ampm,hour,min
        cd = datetime.datetime.now()
        chour = cd.strftime("%I")
        chour = int(chour)
        cmin = cd.strftime("%M")
        cmin = int(cmin)
        campm = cd.strftime("%p")
        if ampm == campm:
            if hour == chour:
                if min == cmin:
                    music("jyotiba.mp3","stop")

                    def ren():
                        
                        try:
                            re = int(input("Enter 1 to reset alarm or 0 to exit the alarm: "))
                            if re == 1:
                                user()
                                alarm()
                            elif re == 0:
                                def end(file):
                                    mixer.init()
                                    mixer.music.load(file)
                                    mixer.music.play(-1)
                                    print("Thank you! By Vinayak Maskar!")

                                    while True:
                                        time.sleep(2)

                                        mixer.music.stop()
                                        break

                                end("thank3.mp3")
                            else:
                                print("Enter 1 or 2!!")
                                ren()

                        except Exception as error:
                            print("Enter 1 or 0!")
                            return ren()

                    ren()

                    break

alarm()













