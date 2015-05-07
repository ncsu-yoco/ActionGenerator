from Story import Story
from HashTable import HashTable
import Printer as styler

xnor = lambda var1, var2 : not (var1 ^ var2)

previousStates = []

# generates a new tuple
def generateTuple(tup, var, keyset, tupleLength):

	newTuple = []

	for i in range(0, tupleLength - 1):
		if tup[i] not in keyset:
			newTuple.append(tup[i])
		else:
			idx = keyset.index(tup[i])
			newTuple.append(var[idx])

	newTuple.append(tup[tupleLength - 1])
	
	return tuple(newTuple)

# find index in dictionary array with given key and value
def findIndex(dictArr, key, value):
	for index in range(len(dictArr)):
		if(dictArr[index][key]==value):
			return dictArr[index]
	return -1

# check if the state is repeated
def repeatedState(dictArr):
	try:
		if previousStates.index(sorted(dictArr)) != -1:
			return True
	except:
		pass
	previousStates.append(sorted(dictArr))
	return False


# planner class
class Planner:

	story = None
	newActions = None

	# initialize the story
	def __init__(self, storyTitle):
		self.story = Story(storyTitle)
		
	# print the current state of the story world
	def printWorld(self):
		for edge in self.story.actions:
			print styler.printState(edge)

	# print curent state of story world
	def printWorldState(self):
		if repeatedState(self.story.edge):
			styler.printHeader("Current World State - REPEATED")
		else:	
			styler.printHeader("Current World State")
		for e in self.story.edge:
			print styler.printState(e)

	# generates next set of actions which user can take
	def nextActions(self, removeDups):
		self.newActions = []
		for act in self.story.actions:
			self.validActions(act, removeDups)
		if(removeDups):
			ht = HashTable()
			removeEle = []
			for act in self.newActions:
				if ht.isPresent(act):
					removeEle.append(act)
					continue
				if(len(act['values']) != len(set(act['values']))):
					removeEle.append(act)
					continue
				ht.add(act)
			for delAct in removeEle:
				self.newActions.remove(delAct)
			ht.destroy()
		return self.newActions

	
	# generate list of valid actions
	def validActions(self, action, sort):
		possibleValues = {}		
		for key in action['parameters'].keys():
			possibleValues[key] = self.story.entities[action['parameters'][key]]
		# if number of parameters are 3
		if(len(action['parameters'].keys()) == 3):
			keyset = sorted(possibleValues.keys())
			for var1 in possibleValues[keyset[0]]:
				for var2 in possibleValues[keyset[1]]:
					for var3 in possibleValues[keyset[2]]:
						found = True
						for pre_cond in action['pre_conditions']:
							tupleLen = len(pre_cond)
							newTuple = generateTuple(pre_cond,[var1,var2,var3],keyset,tupleLen)
							truth = newTuple[:tupleLen-1] in self.story.edge
							if not xnor(truth, newTuple[tupleLen-1]):
								found = False
						if found:
							varList = [var1, var2, var3]
							if(sort):
								varList.sort()
							self.newActions.append({'action':action['do'], 'values':varList})
		# if number of parameters are 2
		if(len(action['parameters'].keys()) == 2):
			keyset = sorted(possibleValues.keys())
			for var1 in possibleValues[keyset[0]]:
				for var2 in possibleValues[keyset[1]]:
					found = True
					for pre_cond in action['pre_conditions']:
						tupleLen = len(pre_cond)
						newTuple = generateTuple(pre_cond,[var1,var2],keyset,tupleLen)
						truth = newTuple[:tupleLen-1] in self.story.edge
						if not xnor(truth, newTuple[tupleLen-1]):
							found = False
					if found:
						varList = [var1,var2]
						if(sort):
							varList.sort()
						self.newActions.append({'action':action['do'], 'values':varList})
		# if number of parameters are 1
		if(len(action['parameters'].keys()) == 1):
			keyset = sorted(possibleValues.keys())
			for var1 in possibleValues[keyset[0]]:
					found = True
					for pre_cond in action['pre_conditions']:
						tupleLen = len(pre_cond)
						newTuple = generateTuple(pre_cond,[var1],keyset,tupleLen)
						truth = newTuple[:tupleLen-1] in self.story.edge
						if not xnor(truth, newTuple[tupleLen-1]):
							found = False
					if found:
						varList = [var1]
						if(sort):
							varList.sort()
						self.newActions.append({'action':action['do'], 'values':varList})

	# perform action as selected by user
	def performAction(self, actionId):
		action = findIndex(self.story.actions, 'do', self.newActions[actionId]['action'])
		if(action == -1):
			print 'Cannot perform action'
			return False
		values = self.newActions[actionId]['values']
		keyset = sorted(action['parameters'].keys())
		for post_cond in action['post_conditions']:
			tupleLen = len(post_cond)
			newTuple = generateTuple(post_cond, values, keyset, tupleLen)
			if newTuple[tupleLen-1]:  
				self.story.edge.append(newTuple[:tupleLen-1])
			else:
				self.story.edge.remove(newTuple[:tupleLen-1])
		return {'act_text':action['action_text'], 'values': values}

	# check if the number of demons are greater than number of saints at any bank. If so, we have failed the goal
	def checkState(self):
		demonLB = 0
		demonRB = 0
		saintLB = 0
		saintRB = 0
		for e in self.story.edge:
			if 'LEFT-BANK' in e:
				if e[0][0] == 'S':
					saintLB += 1
				elif e[0][0] == 'D':
					demonLB += 1
			else:
				if e[0][0] == 'S':
					saintRB += 1
				elif e[0][0] == 'D':
					demonRB += 1
		if(saintRB < demonRB and saintRB != 0) or (saintLB < demonLB and saintLB != 0):
			print "Demons ate the saints"
			print "you lost!"
			return True
		return False