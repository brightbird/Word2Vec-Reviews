#Describes an object or entity being reviewed (a product (Amazon), business (Yelp), etc.)

import numpy as np, gensim
import Review, Word

#Global method: compute cosine similarity of vectors
def cosine_similarity(vec1, vec2):
	return np.dot(vec1, vec2)/(np.linalg.norm(vec1) * np.linalg.norm(vec2))

class Product:
	#Reviews are a list of Review objects: each Review object has a list of words and a rating
	def __init__(self, reviews = [], topic = None, query = [], words = dict(), w2v_model = None):
		self.reviews = reviews #list of all reviews for this product/business
		self.topic = topic #topic word for this product/business (may be the title of the business, or category)
		self.query = query
		self.words = words #keys: words   values: word objects (contains relevance to topic and ratings of reviews using the word)
		self.w2v_model = w2v_model #word2vec model to be used for word comparisons

	#Get cosine similarity of averages of groups of word vectors
	def group_similarity(self, words1, words2):
		#get average vectors
		avg_vec1 = self.w2v_model[words1[0]]
		#sum vectors together elementwise
		for word1_index in range(1,len(words1)):
			avg_vec1 += self.w2v_model[words1[word1_index]]
		avg_vec1 = avg_vec1 / len(words1) #normalize by number of vectors there were

		avg_vec2 = self.w2v_model[words2[0]]
		#sum vectors together elementwise
		for word2_index in range(1,len(words2)):
			avg_vec2 += self.w2v_model[words2[word2_index]] #normalize by number of vectors there were
		avg_vec2 = avg_vec2 / len(words2)
		return cosine_similarity(avg_vec1, avg_vec2)

	#For each word in the review, classify its importance relative to the topic label and possibly additional user queries and assign it a sentiment
	def compute_word_info(self, review):
		for word in review.getText():
			if word in self.w2v_model: #make sure we have a word2vec representation for this word (otherwise ignore)
				if word not in self.words: #this is not a word seen before and it's a word we can process
					#relevance = self.w2v_model.similarity(self.topic, word) #how relevant is this word to the product's topic?
					relevance = self.group_similarity([self.topic] + self.query, [word])
					ratings = {review.getRating() : 1} #1 instance of this rating seen so far, none for the others
					word_object = Word.Word(word, relevance, ratings) #create a new word object with this information
					self.words[word] = word_object #add it to the words dictionary
				else:
					self.words[word].add_rating(review.getRating()) #add this rating to the Word object for this word
	
	#Get word info for each word in each review
	def compute_product_word_info(self):
		for review in self.reviews:
			self.compute_word_info(review)

	#sort words by relevance or positive/negative review counts and print each word + relevance as well as a count of all its reviews
	#TODO possibly count the number of reviews in which the word occurs at all instead of the number of times it appears period
	def print_word_sentiments(self, sortby="relevance"):	
		word_objects = self.words.values()
		if sortby == "relevance": #sort reviews by greatest relevance to the topic
			word_objects.sort(key = lambda word: word.getRelevance()*-1) #take negative to sort in descending order
		elif sortby == "positive": #TODO sort by largest number of positive reviews
			pass
		elif sortby == "negative": #TODO sort by largest number of negative reviews
			pass

		num_top = 10
		for word in word_objects[:num_top]:
			#print out the word and its relevance to the topic
			print("%s (relevance %f to topic %s and " % (word.getWord(), word.getRelevance(), self.topic)), self.query
			#print out number of times word gets each rating that it does #TODO make it print 0 for ratings it never gets
			word_ratings = word.getRatings()
			for rating in word_ratings:
				print("Count of rating %d: %d" % (rating, word_ratings[rating]))
			print

	#update reviews
	def setReviews(self, reviews):
		self.reviews = reviews

	#get reviews
	def getReviews(self):
		return self.reviews

	#update topic
	def setTopic(self, topic):
		self.topic = topic

	#get topic
	def getTopic(self):
		return self.topic

	#update query
	def setQuery(self, query):
		self.query = query

	#get query
	def getQuery(self):
		return self.query

	#update word objects
	def setWords(self, words):
		self.words = words

	#get word objects
	def getWords(self):
		return self.words

	#set word information for individual word with a new word object
	def setWord(self, word, word_object):
		self.words[word] = word_object

	#get individual word information (return word object corresponding to that word)
	def getWord(self, word):
		return self.words[word]

	#update w2v model (if you must...?)
	def setw2v(self, w2v):
		self.w2v_model = w2v

	#get w2v model
	def getw2v(self, w2v):
		return self.w2v_model
