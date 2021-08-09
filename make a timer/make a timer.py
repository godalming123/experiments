from time import *

def getInt (question):
    while True:
        try:
            return int(input (question))
        except:
            print("please enter a real number!")

while True :
	secs = getInt ("seconds: ")
	mins = getInt ("minutes: ")
	hours = getInt ("hours: ")
	
		
	while True :
		print (hours, ":", mins, ":", secs)
		sleep (1)

		if secs > 0 :
			secs -= 1

		elif mins > 0:
			mins -= 1
			secs = 59
			
		elif hours > 0:
			hours -= 1
			mins = 59
			secs = 59

		else :
			break
