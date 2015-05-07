class Story:

	def __init__(self, storyName):
		if storyName == "saintDevilGame":
			self.buildSaintDevil()
		# we can add multiple stories here
		else:
			print "Cannot find story ", storyName
		print "Created ", self.title,"..."

	# saint devil game story structure
	def buildSaintDevil(self):
		self.title = "Saint Devil Game"
		self.entities = {}
		# entities involved in the story
		self.entities['actor'] = ["S1", "S2", "S3", "D1", "D2", "D3"]
		self.entities['location'] = ["LEFT-BANK", "RIGHT-BANK"]
		# set of conditions true in the world at start
		self.edge = [
				("S1", "AT", "LEFT-BANK"),
				("S2", "AT", "LEFT-BANK"),
				("S3", "AT", "LEFT-BANK"),
				("D1", "AT", "LEFT-BANK"),
				("D2", "AT", "LEFT-BANK"),
				("D3", "AT", "LEFT-BANK"),
				("BOAT", "AT", "LEFT-BANK") ]
		# set of actions actors can take
		self.actions = [
						{'do' : 'ROW-LEFT',							# name of actions
						'parameters' : {							# variables for given action
							'1Passenger1' : 'actor',
							'2Passenger2' : 'actor' },	
						'pre_conditions' : [						# set of pre-conditions
							("1Passenger1", "AT", "RIGHT-BANK", True),
							("2Passenger2", "AT", "RIGHT-BANK", True),
							("BOAT", "AT", "RIGHT-BANK", True) ],
						'post_conditions' : [						# set of post consitions
							("1Passenger1", "AT", "RIGHT-BANK", False),
							("2Passenger2", "AT", "RIGHT-BANK", False),
							("BOAT", "AT", "RIGHT-BANK", False),
							("1Passenger1", "AT", "LEFT-BANK", True),
							("2Passenger2", "AT", "LEFT-BANK", True),
							("BOAT", "AT", "LEFT-BANK", True) ],
						'action_text' : '&1 and &2 sat in the boat and rowed to left bank. '	# text template for printing the action
						},
						# another action
						{'do' : 'ROW-RIGHT',
						'parameters' : {
							'1Passenger1' : 'actor',
							'2Passenger2' : 'actor' },
						'pre_conditions' : [
							("1Passenger1", "AT", "LEFT-BANK", True),
							("2Passenger2", "AT", "LEFT-BANK", True),
							("BOAT", "AT", "LEFT-BANK", True) ],
						'post_conditions' : [
							("1Passenger1", "AT", "LEFT-BANK", False),
							("2Passenger2", "AT", "LEFT-BANK", False),
							("BOAT", "AT", "LEFT-BANK", False),
							("1Passenger1", "AT", "RIGHT-BANK", True),
							("2Passenger2", "AT", "RIGHT-BANK", True),
							("BOAT", "AT", "RIGHT-BANK", True) ],
						'action_text' : '&1 and &2 sat in the boat and rowed to right bank. '
						},
						# another action
						{'do' : 'ROW-RIGHT-ALONE',
							'parameters' : {
								'1Passenger1' : 'actor'},
							'pre_conditions' : [
								("1Passenger1", "AT", "LEFT-BANK", True),
								("BOAT", "AT", "LEFT-BANK", True) ],
							'post_conditions' : [
								("1Passenger1", "AT", "LEFT-BANK", False),
								("BOAT", "AT", "LEFT-BANK", False),
								("1Passenger1", "AT", "RIGHT-BANK", True),
								("BOAT", "AT", "RIGHT-BANK", True) ],
						'action_text' : '&1 sat in the boat and rowed to right bank alone. '
						},
						# another action
						{'do' : 'ROW-LEFT-ALONE',
							'parameters' : {
								'1Passenger1' : 'actor'},
							'pre_conditions' : [
								("1Passenger1", "AT", "RIGHT-BANK", True),
								("BOAT", "AT", "RIGHT-BANK", True) ],
							'post_conditions' : [
								("1Passenger1", "AT", "RIGHT-BANK", False),
								("BOAT", "AT", "RIGHT-BANK", False),
								("1Passenger1", "AT", "LEFT-BANK", True),
								("BOAT", "AT", "LEFT-BANK", True) ],
							'action_text' : '&1 sat in the boat and rowed to left bank alone. '
						}
						]
