import pickle
from sklearn.cluster import KMeans

# Load the TF-IDF matrix
with open('tfidf_matrix.pkl', 'rb') as file:
    tfidf_matrix = pickle.load(file)

# Load the feature names
with open('tfidf_features.pkl', 'rb') as file:
    feature_names = pickle.load(file)


def perform_kmeans(n_clusters, data):
    km = KMeans(n_clusters=n_clusters, random_state=42)
    km.fit(data)
    return km.labels_, km.cluster_centers_

labels_3, centers_3 = perform_kmeans(3, tfidf_matrix)
labels_6, centers_6 = perform_kmeans(6, tfidf_matrix)


def top_terms_per_cluster(n_terms, centers):
    top_terms = {}
    for i, center in enumerate(centers):
        top_indices = center.argsort()[-n_terms:][::-1] 
        top_features = [feature_names[index] for index in top_indices]
        top_terms[i] = top_features
    return top_terms

top_terms_3 = top_terms_per_cluster(10, centers_3)
top_terms_6 = top_terms_per_cluster(10, centers_6)

# Display top terms for each cluster
print("Top terms for 3 clusters:")
for cluster, terms in top_terms_3.items():
    print(f"Cluster {cluster}: {', '.join(terms)}")

print("\nTop terms for 6 clusters:")
for cluster, terms in top_terms_6.items():
    print(f"Cluster {cluster}: {', '.join(terms)}")
