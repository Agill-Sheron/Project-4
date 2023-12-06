import pickle
from sklearn.cluster import KMeans

def perform_clustering(tfidf_matrix_file, tfidf_features_file, n_clusters, n_terms):
    with open(tfidf_matrix_file, 'rb') as file:
        tfidf_matrix = pickle.load(file)

    with open(tfidf_features_file, 'rb') as file:
        feature_names = pickle.load(file)

    km = KMeans(n_clusters=n_clusters, random_state=42)
    km.fit(tfidf_matrix)
    labels = km.labels_
    centers = km.cluster_centers_
    
    top_terms = {}
    for i, center in enumerate(centers):
        top_indices = center.argsort()[-n_terms:][::-1]
        top_features = [feature_names[index] for index in top_indices]
        top_terms[i] = top_features
    
    return labels, top_terms

if __name__ == "__main__":
    tfidf_matrix_file = 'tfidf_matrix.pkl'
    tfidf_features_file = 'tfidf_features.pkl'
    n_clusters = 3 
    labels, centers, top_terms = perform_clustering(tfidf_matrix_file, tfidf_features_file, n_clusters)
