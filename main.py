#Run the program to process reviews
import sys
from Product import *
from preprocess import preprocess_data_manual

def main():
	data_file = sys.argv[1]
	topic = sys.argv[2]
	queries = sys.argv[3:]
	product = preprocess_data_manual(data_file, topic, queries)
	product.compute_product_word_info()
	product.print_word_sentiments()

if __name__ == "__main__":
	main()
