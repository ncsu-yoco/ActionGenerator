#!/usr/bin/python
# To aid printing

import string

# prints formatted text for actions and states of the story world

# title for section
def printHeader(str):
	print "\t\t\t*******************************************"
	print "\t\t\t***    ", str
	print "\t\t\t*******************************************"

# action : as presented to user to choose
def printAction(id,act):
	if(act=="Exit"):
		return "\t" + str(id) + ":\t" + "Finish Story"
	return "\t" + str(id) + ":\t" + act['action'] + " with " + ' and '.join(act['values'])

# current state of the system
def printState(state):
	return "\t" + ' '.join(state)

# adds text to story based on selected action
def addStoryText(act):
	retVal =  act['act_text']
	for i in range(len(act['values'])):
		retVal = retVal.replace("&" + str(i+1), act['values'][i])
	return retVal