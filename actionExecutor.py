import sys
import re
import time

dogLastFed = "never"

def turnOnTV():
	print "Turning on tv"

def turnOnSecTV():
	print "Turning on second TV"

def turnOnReceiver():
	print "Turning on receiver"

def turnOnSystem():
	print "Turning on system"

def turnOffTV():
	print "Turning off TV"

def turnOffSecTV():
	print "Turning off second TV"

def turnOffReceiver():
	print "Turning off receiver"

def turnOffSystem():
	print "Turning off system"

def statusReport():
	print "Giving status report"

def dogLastFed():
	print "The dog was last fed", dogLastFed

def fedDog():
	global dogLastFed
	dogLastFed = time.strftime("%a") + " " + time.strftime("%H")
	print "Dog fed on", dogLastFed

strToFunct = {
	#Turn of the first tv
"TURN OFF TV" : turnOffTV,
"TURN OFF THE TV" : turnOffTV,
	#turn on the first tv
"TURN ON TV" : turnOnTV,
"TURN ON THE TV" : turnOnTV,
	#turn off the receiver
"TURN OFF RECEIVER" : turnOfReceiver,
"TURN OFF THE RECEIVER" : turnOffReceiver,
	#turn on the receiver
"TURN OFF SECOND TV" : turn	

print "Listening...  (Give it a couple seconds)"
while True:
	line = sys.stdin.readline()
	line = re.sub("\w*: ", "",line, 1)
	if line.
