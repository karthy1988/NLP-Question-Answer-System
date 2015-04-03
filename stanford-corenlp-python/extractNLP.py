## VERSION 2
## Note: Changes in input, takes dictionary output py Parse module


class Extract(object):
	def __init__(self,parse,level=1):
		"""Extracts phrase strings from list at the given level is the parse tree. If provided level is invalid, will return phrases of highest order.
		If no phrase exists, will return None type."""
		self.parseList = parse["parsedSentence"]
		self.raw = parse["rawSentence"]
		self.level = level
		return 

	def getString(self,subParse,acc): 
		if (subParse == []): return ""
		elif all((type(x) == str) for x in subParse): 
			try:
				return (subParse[1] + " ")
			except:
				print subParse
				print "Something Failed :("
		for tok in subParse:
			if (type(tok) == list):
				acc += self.getString(tok," ")
		return acc

		
	def getText(self):
		"""Returns dictionay of (POS,phrase) kv pairs."""
		## ONLY IMPLEMENTED FOR LEVEL 1 NOW...
		print("Retrieving phrases at level %d..." % self.level)
		# if ('S' not in self.parseList):
		# 	print("This is a fragment, try again.")
		# 	return None

		# # Removes 'S' tag and [] end of line
		self.results = dict()
		innerList = []
		for stree in self.parseList[1:]:
			try:
				if (stree[0] == 'S'):
					innerList += stree[1:]
				else:
					innerList.append(stree)
			except:
				# print stree
				# Random [] in sentences... IDK why
				# also random ['POS'] ohh is punctuation like '.'
				print "Empty.. ignore"
		for sub in innerList:
			if (sub == []): pass 
			else:
				pos = sub[0]
				string = self.getString(sub[1:],"")
				string = string.replace('  ', ' ')
				try:
					if string[0] == " ": 
						string = string[1:]
				except: pass
				try:
					tmp = self.results[pos]
					rself.esults[pos] = tmp.append(string)
				except:
					self.results[pos] = [string]
		return self.results






















