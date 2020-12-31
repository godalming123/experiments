from time import *
while True :
		running = True
		sec = input ("seconds: ")
		minutes = input ("minutes: ")
		hours = input ("hours: ")

		try :
				sec = int (sec)
				minutes	= int (minutes)
				hours = int (hours)
		except :
				print (hours, ", ", sec, "or", minutes, " is not a valid number")
				running = False
		
		while running :
				print (hours, ":", minutes, ":", sec)
				sleep (1)

				if sec > 0 :
					sec -= 1
				elif minutes > 0:
					minutes -= 1
					sec = 59
				elif hours > 0:
					hours -= 1
					minutes = 59
					sec = 59
