#Define class for Word objects
#Each Word contains a relevance to the topic word and a list of ratings of reviews in which it occurs

class Word:
	def __init__(self, word, relevance=None, ratings=dict()):
		self.word = word
		self.relevance = relevance
		self.ratings = ratings

	#update the word for this word object (maybe should just create a new object?)
	def setWord(self, word):
		self.word = word

	#get the word for this word object
	def getWord(self):
		return self.word

	#update the relevance to a review
	def setRelevance(self, relevance):
		self.relevance = relevance

	#get the relevance of a review
	def getRelevance(self):
		return self.relevance

	#update the list of review ratings (use if you have to overhaul ratings list significantly)
	def setRatings(self, ratings):
		self.ratings = ratings

	#just append a new review rating to existing list of review ratings
	def add_rating(self, review_rating):
		if review_rating not in self.ratings:
			self.ratings[review_rating] = 0 #add this rating to dictionary of known ratings
		self.ratings[review_rating] += 1

	#get the list of ratings a word occurs in
	def getRatings(self):
		return self.ratings
