import spacy
from spacy.lang.en.stop_words import STOP_WORDS

# Load SpaCy's English language model
nlp = spacy.load('en_core_web_sm')

# Example text
text = "Hello world! This is a simple example to demonstrate tokenization, stop words removal, stemming, and lemmatization."

# Tokenization
print("Tokenization:")
doc = nlp(text)
words = [token.text for token in doc]
sentences = [sent.text for sent in doc.sents]
print("Words:", words)
print("Sentences:", sentences)

# Stop Words Removal
print("\nStop Words Removal:")
filtered_words = [word for word in words if word.lower() not in STOP_WORDS]
print("Filtered Words:", filtered_words)

# Stemming (using SpaCy's Lemmatization)
print("\nStemming (using SpaCy's Lemmatization):")
stemmed_words = [token.lemma_ for token in doc if token.text.lower() not in STOP_WORDS]
print("Stemmed Words:", stemmed_words)

# Lemmatization
print("\nLemmatization:")
lemmatized_words = [token.lemma_ for token in doc if token.text.lower() not in STOP_WORDS]
print("Lemmatized Words:", lemmatized_words)
