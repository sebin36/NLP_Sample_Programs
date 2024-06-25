import nltk

# Download the necessary NLTK data files
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('omw-1.4')
nltk.download('wordnet')

from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer

# Example text
text = "Hello world! This is a simple example to demonstrate tokenization, stop words removal, stemming, and lemmatization."

# Tokenization
print("Tokenization:")
words = word_tokenize(text)
print("Words:", words)

sentences = sent_tokenize(text)
print("Sentences:", sentences)

# Stop Words Removal
print("\nStop Words Removal:")
stop_words = set(stopwords.words('english'))
filtered_words = [word for word in words if word.lower() not in stop_words]
print("Filtered Words:", filtered_words)

# Stemming
print("\nStemming:")
stemmer = PorterStemmer()
stemmed_words = [stemmer.stem(word) for word in filtered_words]
print("Stemmed Words:", stemmed_words)

# Lemmatization
print("\nLemmatization:")
lemmatizer = WordNetLemmatizer()
lemmatized_words = [lemmatizer.lemmatize(word, pos='v') for word in filtered_words]  # pos='v' for verbs
print("Lemmatized Words:", lemmatized_words)
