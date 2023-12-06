import argparse
from robots import fetch_and_save_robots_info
from crawler import start_crawling
from parsing import start_parsing
from preprocess import preprocess
from vectorization import perform_vectorization
from clustering import perform_clustering
from sentiment_analysis import get_cluster_sentiments
from tqdm import tqdm

def save_top_terms(top_terms, filename):
    with open(filename, 'w') as file:
        for cluster, terms in top_terms.items():
            file.write(f"Cluster {cluster + 1}: {', '.join(terms)}\n")

def save_sentiment_analysis(cluster_sentiments, filename):
    with open(filename, 'w') as file:
        for cluster, sentiment in cluster_sentiments.items():
            file.write(f"Cluster {cluster + 1}: Average Sentiment = {sentiment}\n")


def main(max_urls):
    # Directory paths
    start_url = "https://www.concordia.ca"
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
        labels_3, top_terms_3 = perform_clustering(tfidf_matrix_file, tfidf_features_file, 3, 20)
        pbar.update(1)
    
        pbar.set_description("Clustering k=6")
        labels_6, top_terms_6 = perform_clustering(tfidf_matrix_file, tfidf_features_file, 6, 20)
        pbar.update(1)
    
        pbar.set_description("Sentiment Analysis")
        cluster_sentiments_3 = get_cluster_sentiments(preprocessed_dir, labels_3)
        cluster_sentiments_6 = get_cluster_sentiments(preprocessed_dir, labels_6)
        pbar.update(1)

    
    save_top_terms(top_terms_3, 'top_terms_3_clusters.txt')
    save_top_terms(top_terms_6, 'top_terms_6_clusters.txt')
    save_sentiment_analysis(cluster_sentiments_3, 'sentiment_analysis_3_clusters.txt')
    save_sentiment_analysis(cluster_sentiments_6, 'sentiment_analysis_6_clusters.txt')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Web Crawling and Analysis Script')
    parser.add_argument('-max', '--max_urls', type=int, default=1000, help='Maximum number of URLs to crawl')
    args = parser.parse_args()

    main(max_urls=args.max_urls)