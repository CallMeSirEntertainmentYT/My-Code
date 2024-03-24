import time
import threading

seconds = 0
minutes = 0
hours = 0
running = True

print('Thank you for using Advanced Timer. Type "check" at any time to check the time.')

def check_time():
	while running:
		time.sleep(1)
		global seconds, minutes, hours
		seconds += 1
		if seconds == 60:
			seconds = 0
			minutes += 1
		if minutes == 60:
			minutes = 0
			hours += 1

def check_input():
	while running:
		checking = input()
		if checking == "check":
			print("Current time passed:", hours, "hours,", minutes, "minutes, and", seconds, "seconds.")

threading.Thread(target=check_time).start()
threading.Thread(target=check_input).start()


	