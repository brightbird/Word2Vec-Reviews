#Preprocess review data and store it as review objects
import string, gensim
import Review, Product

#Preprocess data in the Yelp format
def preprocess_data(data_file):
	pass

#Preprocess data in the Reuters/Twitter format: review on its own line, tab separates label from text
#Just remove punctuation and create product object; don't remove stop words etc
def preprocess_data_manual(data_file, reviews_topic, reviews_query):
	raw_reviews = list(open(data_file, "r"))
	reviews = list()
	for raw_review in raw_reviews:
		review_split = raw_review.split("\t") #separate label from review
		label = int(review_split[0])
		#strip trailing whitespace, lowercase (NOTE: w2v is case sensitive...on the balance hopefully this is beneficial) remove punctuation
		no_punctuation = review_split[1].rstrip().lower().translate(string.maketrans("",""), string.punctuation)
		review_text = no_punctuation.split()
		review = Review.Review(label, review_text)
		reviews.append(review)
	product = Product.Product(reviews, topic=reviews_topic, query=reviews_query, w2v_model = gensim.models.Word2Vec.load("../WMD_code/GoogleNews_vectors"))
	return product 
