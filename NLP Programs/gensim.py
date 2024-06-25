import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from gensim.parsing.preprocessing import remove_stopwords
from gensim.parsing.porter import PorterStemmer
import spacy

# Load SpaCy's English language model
nlp = spacy.load('en_core_web_sm')

# Example text
text = "Hello world! This is a simple example to demonstrate tokenization, stop words removal, stemming, and lemmatization."

# Tokenization
print("Tokenization:")
words = word_tokenize(text)
sentences = sent_tokenize(text)
print("Words:", words)
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

# Lemmatization using SpaCy
print("\nLemmatization:")
doc = nlp(' '.join(filtered_words))
lemmatized_words = [token.lemma_ for token in doc]
print("Lemmatized Words:", lemmatized_words)
