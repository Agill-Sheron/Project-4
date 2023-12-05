from robots import fetch_and_save_robots_info
from crawler import start_crawling
from parsing import start_parsing
from preprocess import preprocess
from vectorization import perform_vectorization
from clustering import perform_clustering, print_top_terms
from sentiment_analysis import get_cluster_sentiments
from tqdm import tqdm

def main():
    # Directory paths
    start_url = "https://www.concordia.ca"
    max_urls = 1000
    depth_limit = 3
    html_dir = './html'
    parsed_dir = './parsed'
    preprocessed_dir = './preprocessed'
    tfidf_matrix_file = 'tfidf_matrix.pkl'
    tfidf_features_file = 'tfidf_features.pkl'

    with tqdm(total=7) as pbar:
        pbar.set_description("Checking robots.txt")
        fetch_and_save_robots_info(start_url + "/robots.txt", "robots_info.txt")
        pbar.update(1)
    
        pbar.set_description("Crawling")
        start_crawling(start_url, max_urls, depth_limit, html_dir)
        pbar.update(1)
    
        pbar.set_description("Parsing HTML")
        start_parsing(html_dir, parsed_dir)
        pbar.update(1)

        pbar.set_description("Preprocessing Text")
        preprocess(parsed_dir, preprocessed_dir)
        pbar.update(1)
    
        pbar.set_description("Vectorizing")
        perform_vectorization(preprocessed_dir, tfidf_matrix_file, tfidf_features_file)
        pbar.update(1)
    
        pbar.set_description("Clustering k=3")
        labels_3, top_terms_3 = perform_clustering(tfidf_matrix_file, tfidf_features_file, 3, 10)
        pbar.update(1)
    
        pbar.set_description("Clustering k=6")
        labels_6, top_terms_6 = perform_clustering(tfidf_matrix_file, tfidf_features_file, 6, 10)
        pbar.update(1)
    
        pbar.set_description("Sentiment Analysis")
        cluster_sentiments_3 = get_cluster_sentiments(preprocessed_dir, labels_3)
        cluster_sentiments_6 = get_cluster_sentiments(preprocessed_dir, labels_6)
        pbar.update(1)


    # Print top terms  
    print("\nTop terms for 3 clusters:")
    print_top_terms(top_terms_3)
    
    print("\nTop terms for 6 clusters:")
    print_top_terms(top_terms_6)

    # Print cluster sentiments
    print("Cluster Sentiments for 3 Clusters:", cluster_sentiments_3)
    print("Cluster Sentiments for 6 Clusters:", cluster_sentiments_6)

if __name__ == "__main__":
    main()
