from sklearn.feature_extraction.text import TfidfVectorizer
import os
import pickle

def read_preprocessed_files(directory):
    documents = []
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as file:
            documents.append(file.read())
    return documents

# Read preprocessed text files
preprocessed_dir = './preprocessed'
texts = read_preprocessed_files(preprocessed_dir)

# Create a TF-IDF Vectorizer
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(texts)

# tfidf_matrix now contains the TF-IDF vectors for the documents
from sklearn.feature_extraction.text import TfidfVectorizer
import os

# Save the TF-IDF matrix
with open('tfidf_matrix.pkl', 'wb') as file:
    pickle.dump(tfidf_matrix, file)

# Optionally, save the feature names (words) for later reference
with open('tfidf_features.pkl', 'wb') as file:
    pickle.dump(vectorizer.get_feature_names_out(), file)
