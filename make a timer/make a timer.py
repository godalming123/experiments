from time import *

def getInt (prompt) :
	num = input(prompt)
	try:
		return int(num)
	except:
		print(num, "is not a valid integer \n")
		return getInt(prompt)

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