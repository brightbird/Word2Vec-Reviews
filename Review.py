#Defines the class for Reviews
#Each word has a rating and a list of words in the review

class Review():
	#Initialize instance variables with user-supplied values
	def __init__(self, rating=None, text=[]):
		self.rating = rating
		self.text = text

	#update rating for a review	
	def setRating(self, rating):
		self.rating = rating
	
	#get rating for a review
	def getRating(self):
		return self.rating

	#update text for a review
	def setText(self, text):
		self.text = text
	
	#get text for a review
	def getText(self):
		return self.text
