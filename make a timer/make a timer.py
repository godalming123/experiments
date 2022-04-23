from time import *

def getInt (question):
    while True:
        try:
            return int(input (question))
        except:
            print("please enter a real number!")

while True :
	print("How long do you want your timer to be.")
	secs = getInt ("seconds: ")
	mins = getInt ("minutes: ")
	hours = getInt ("hours: ")
	days = getInt ("days: ")
		
	while True :
		print ("DAY: ", days, "TIME: ", hours, ":", mins, ":", secs)
		sleep (1)

		if secs > 0 :
			secs -= 1

		elif mins > 0:# if the seconds are zero and the minutes are above zero
			mins -= 1
			secs = 59
			
		elif hours > 0:# if the minutes are zero and the seconds are 0 and the hours are above zero
			hours -= 1
			mins = 59
			secs = 59
				
		elif days > 0:# if the minutes are zero and the seconds are 0 and the hours are 0 and the days are above zero
			days -= 1
			hours = 23
			mins = 59
			secs = 59

		else :
			print("timer finished!")
			break
