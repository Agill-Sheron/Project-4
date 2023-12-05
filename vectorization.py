from sklearn.feature_extraction.text import TfidfVectorizer
import os
import pickle

def perform_vectorization(preprocessed_dir, tfidf_matrix_file, tfidf_features_file):
    documents = read_preprocessed_files(preprocessed_dir)

    # Adjusted TF-IDF Vectorizer settings
    vectorizer = TfidfVectorizer(max_df=0.5)
    tfidf_matrix = vectorizer.fit_transform(documents)

    # Save the TF-IDF matrix and feature names
    with open(tfidf_matrix_file, 'wb') as file:
        pickle.dump(tfidf_matrix, file)
    with open(tfidf_features_file, 'wb') as file:
        pickle.dump(vectorizer.get_feature_names_out(), file)

    return tfidf_matrix, vectorizer.get_feature_names_out()

def read_preprocessed_files(directory):
    documents = []
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as file:
            documents.append(file.read())
    return documents

if __name__ == "__main__":
    preprocessed_dir = './preprocessed'
    tfidf_matrix_file = 'tfidf_matrix.pkl'
    tfidf_features_file = 'tfidf_features.pkl'
    
    perform_vectorization(preprocessed_dir, tfidf_matrix_file, tfidf_features_file)
