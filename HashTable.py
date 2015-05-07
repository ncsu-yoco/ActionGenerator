#!usr/bin/python

# implements hash table dictionary for faster access of items
class HashTable:
	
	hash_table = {}

	# initliaze
	def __init__(self):
		pass

	# add new key to hash table
	# 		key is typecasted to str, as dictionaries are non hashable items
	def add(self, key):
		self.hash_table[str(key)] = 'True'

	# print all keys in given table
	def printKeys(self):
		for key in self.hash_table.keys():
			print ">>",key

	# check if given key is present in the hash table
	def isPresent(self, item):
		try:
			present = self.hash_table[str(item)]
		except KeyError:
			return False
		return True

	# get value associated with particular key in the hash table
	def get(self, key):
		if(self.isPresent(str(key))):
			return self.hash_table[key]
		return None

	# remove key from th hash table
	def remove(self, key):
		try:
			del self.hash_table[str(key)]
		except:
			pass

	# delete all keys present in the hash table
	def destroy(self):
		for key in self.hash_table.keys():
			try:
				del self.hash_table[str(key)]
			except:
				pass