from Story import Story
from Planner import Planner
import subprocess
import Printer as styler

'''Main function for the application'''
if __name__ == "__main__":
	storyTitle = "saintDevilGame"	#inits story with saint devil game
	p = Planner(storyTitle)
	storyText = "\t"
	inp = -1
	while(inp != 0):
		# clear screen on each iteration of story.. for readability
		# UNIX based systems
		try:
			subprocess.call(['clear'])
		except OSError:
			pass
		# Windows systems
		try:
			subprocess.call(['cls'])
		except OSError:
			pass

		# print the story so far
		styler.printHeader("Story so far")
		print storyText

		# print current set of valid conditions in the world
		p.printWorldState()

		# present list of valid conditions in current world
		actions = p.nextActions(True)
		styler.printHeader("Select from following actions")
		
		print styler.printAction(0,"Exit")

		for i in range(len(actions)):
			print styler.printAction(i+1,actions[i])
		try:
			# check if previous action counted towards us failed goal.
			# 		in this case, it would be if number of demons exceed number of saints at given bank,
			#		if so, exit the code
			if p.checkState():
				break
			inp =  int(raw_input('\tSelect Choice: '))
			if(inp>0):
				# perform the listed action and append text to the story
				storyText += styler.addStoryText(p.performAction(inp-1))
		except:
			pass



