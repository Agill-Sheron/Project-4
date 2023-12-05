from clustering import perform_kmeans
import pickle
from afinn import Afinn
import numpy as np
import os

# Load the TF-IDF matrix
with open('tfidf_matrix.pkl', 'rb') as file:
    tfidf_matrix = pickle.load(file)

# Load the feature names
with open('tfidf_features.pkl', 'rb') as file:
    feature_names = pickle.load(file)

labels_3, centers_3 = perform_kmeans(3, tfidf_matrix)
labels_6, centers_6 = perform_kmeans(6, tfidf_matrix)

def read_preprocessed_texts(directory):
    texts = []
    for filename in sorted(os.listdir(directory)):  # Ensure consistent order
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as file:
            texts.append(file.read())
    return texts

# Directory where preprocessed texts are stored
preprocessed_dir = './preprocessed'

# Read preprocessed texts
original_texts = read_preprocessed_texts(preprocessed_dir)

afinn = Afinn()

def get_cluster_sentiments(texts, labels_k):
    cluster_sentiments = {}
    for label in set(labels_k):
        cluster_sentiments[label] = []

    for text, label in zip(texts, labels_k):
        sentiment_score = afinn.score(text)
        cluster_sentiments[label].append(sentiment_score)

    return {label: np.mean(scores) if scores else 0 for label, scores in cluster_sentiments.items()}

# Example usage for k=3 and k=6 clusters
cluster_sentiments_3 = get_cluster_sentiments(original_texts, labels_3)
cluster_sentiments_6 = get_cluster_sentiments(original_texts, labels_6)

print("Cluster Sentiments for 3 Clusters:", cluster_sentiments_3)
print("Cluster Sentiments for 6 Clusters:", cluster_sentiments_6)
