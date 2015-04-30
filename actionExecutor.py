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
	
def volUp():
	print "volume up"

def volDown():
	print "volume down"
	
def toHDMIOne():
	print "Switching to HDMI one"
	
def toHDMITwo():
	print "Switching to HDMI two"
	
def toHDMIThree():
	print "Switching to HDMI three"
	
def toHDMIFour():
	print "Switching to HDMI four"
	
def toTuner():
	print "Switching to the tuner"

#Dictionary that converts all strings to functions
strToFunct = {
	#Turn off the first tv
"TURN OFF TV" : turnOffTV,
"TURN OFF THE TV" : turnOffTV,
	#turn on the first tv
"TURN ON TV" : turnOnTV,
"TURN ON THE TV" : turnOnTV,
	#turn off the receiver
"TURN OFF RECEIVER" : turnOfReceiver,
"TURN OFF THE RECEIVER" : turnOffReceiver,
	#turn on the receiver
"TURN ON RECEIVER" : turnOnReceiver,
"Turn ON THE RECEIVER" : turnOnReceiver,
	#turn off the second tv
"TURN OFF THE SECOND TV" : turnOffSecTV,
"TURN OFF SECOND TV" : turnOffSecTV,
	#turn on second tv
"TURN ON SECOND TV" : turnOnSecTV,
"TURN ON THE SECOND TV" : turnOnSecTV,
	#turn off the system
"POWER OFF" : turnOffSystem,
"TURN OFF" : turnOffSystem,
"POWER DOWN" : turnOffSystem,
"SYSTEM OFF" : turnOffSystem,
"SHUT DOWN" : turnOffSystem,
	#turn on the system
"POWER ON" : turnOnSystem,
"START" : turnOnSystem,
"ALL ON" : turnOnSystem,
	#status report
"STATUS REPORT" : statusReport,
	#fed dog
"I JUST FED THE DOG" : fedDog,
"I FED THE DOG" : fedDog,
	#check dog fed time
"WHEN WAS THE DOG LAST FED" : dogLastFed,
"WHEN WAS THE DOG FED" : dogLastFed
	#volume up
"VOLUME UP" : volUp,
"TURN THE VOLUME UP" :volUp,
	#volume down
"VOLUME DOWN" : volDown,
"TURN THE VOLUME DOWN" : volDown,
	#swith to hdmi input one
"HDMI ONE" : toHDMIOne,
"SWITCH TO HDMI ONE" : toHDMIOne,
	#swith to hdmi input two
"HDMI TWO" : toHDMITwo,
"SWITCH TO HDMI TWO" : toHDMITwo,
	#swith to HDMI input three
"HDMI THREE" : toHDMIThree,
"SWITCH TO HDMI THREE" : toHDMIThree,
	#swith to HDMI input four
"HDMI FOUR" : toHDMIFour,
"SWITCH TO HDMI FOUR" : toHDMIFour,
	#switch to the tuner
"TUNER" : toTuner,
"SWITCH TO TUNER" : toTuner,
"RADIO" : toTuner,
"SWITCH TO RADIO" : toTuner,
}

print "Listening...  (Give it a couple seconds)"
while True:
	line = sys.stdin.readline()
	line = re.sub("\w*: ", "",line, 1)
	if line == '':
		continue
	#split the line at the first whitespace, getting the name and the command
	stringSplit = string.split(line,1)
	name = stringSplit[0]
	command = stringSplit[1]
	print name, command
	
	
