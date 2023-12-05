from afinn import Afinn
import numpy as np
import os

def get_cluster_sentiments(preprocessed_dir, labels_k):
    afinn = Afinn()
    texts = read_preprocessed_texts(preprocessed_dir)

    cluster_sentiments = {}
    for label in set(labels_k):
        cluster_sentiments[label] = []

    for text, label in zip(texts, labels_k):
        sentiment_score = afinn.score(text)
        cluster_sentiments[label].append(sentiment_score)

    return {label: np.mean(scores) if scores else 0 for label, scores in cluster_sentiments.items()}

def read_preprocessed_texts(directory):
    texts = []
    for filename in sorted(os.listdir(directory)):  
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as file:
            texts.append(file.read())
    return texts