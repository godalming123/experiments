from datetime import *
while True :
    running = True
    sec = input ("how long do you want the timer running for in seconds: ")
    minutes = input ("how many minutes do you want the timer to run for: ")
    hours = input ("how many hours do you wnt the timer to run for : ")
    date = date ()
    try :
        sec = int (sec)
        minutes  = int (minutes)
        hours = int (hours)
    except :
        print (hours, ", ", sec, "or", minutes, " is not a valid number")
        running = False
    while running :
        print (hours, ":", minutes, ":", sec)
        sleep (1)
        if sec < 0 and minutes < 0 and hours < 0:
            print ("timer done")
            running = False
        elif minutes < 0 and sec < 0:
            hours -= 1
            minutes = 60
        elif sec < 0 : 
            minutes -= 1
            sec = 60
        sec -= 1
