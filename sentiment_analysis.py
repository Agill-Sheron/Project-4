from afinn import Afinn
import numpy as np
import os

def get_cluster_sentiments(preprocessed_dir, labels_k):
    afinn = Afinn()
    texts = read_preprocessed_texts(preprocessed_dir)

    cluster_sentiments = {}
    cluster_lengths = {}
    for label in set(labels_k):
        cluster_sentiments[label] = []
        cluster_lengths[label] = []

    for text, label in zip(texts, labels_k):
        sentiment_score = afinn.score(text)
        text_length = len(text.split()) 
        cluster_sentiments[label].append(sentiment_score * text_length)  
        cluster_lengths[label].append(text_length)  

    # Calculating weighted average sentiment score for each cluster
    weighted_avg_sentiments = {}
    for label in cluster_sentiments:
        total_weighted_sentiment = sum(cluster_sentiments[label])
        total_length = sum(cluster_lengths[label])
        weighted_avg_sentiments[label] = round(total_weighted_sentiment / total_length if total_length > 0 else 0, 2)

    return weighted_avg_sentiments

def read_preprocessed_texts(directory):
    texts = []
    for filename in sorted(os.listdir(directory)):  
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as file:
            texts.append(file.read())
    return texts