from datetime import *
while True :
    running = True
    sec = input ("seconds: ")
    minutes = input ("minutes: ")
    hours = input ("hours: ")
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
