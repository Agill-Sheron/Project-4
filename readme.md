# Web Crawling and Sentiment Analysis Project

## Project Overview
This project is designed to crawl the Concordia University website, process the extracted text data, perform document clustering, and conduct sentiment analysis on the clustered documents. It represents a comprehensive pipeline from data collection to analysis while adhering to ethical web scraping guidelines.

## Setup and Installation
Ensure Python and the following libraries are installed before running the project:
- Scrapy
- BeautifulSoup
- NLTK
- scikit-learn
- Afinn
- NumPy
- tqdm

Install these packages using pip:
```bash
pip install scrapy beautifulsoup4 nltk scikit-learn afinn numpy tqdm
```

## Files in the Project
- `robots.py`: Fetches and processes `robots.txt` from the Concordia website.
- `crawler.py`: Uses Scrapy to crawl web pages from the Concordia website.
- `parsing.py`: Parses the HTML content and extracts clean text.
- `preprocess.py`: Processes the text data, including tokenization and stop word removal.
- `vectorization.py`: Converts text data into a TF-IDF matrix.
- `clustering.py`: Performs KMeans clustering on the vectorized data.
- `sentiment_analysis.py`: Analyzes the sentiment of the clustered documents.
- `main.py`: Orchestrates the entire crawling, processing, and analysis pipeline, with an adjustable maximum URL parameter.
- `scrapy_spider.py`: Defines the Scrapy spider for web crawling.

## Running the Project
To run the project, use the `main.py` script. You can specify the maximum number of URLs to crawl with the `-max` parameter:
```bash
python main.py --max_urls 500
```
If `-max` is not specified, the script will use a default value. The script executes each process sequentially, tracking progress with a tqdm progress bar.

## Outputs
The project generates several outputs:
- Crawled HTML files from the Concordia website.
- Parsed and preprocessed text data.
- TF-IDF matrix and feature names.
- Cluster labels and top terms for each cluster.
- Sentiment scores for each cluster.

## Ethical Considerations
The project adheres to the web scraping guidelines outlined in Concordia University's `robots.txt` file, promoting ethical data collection practices.

## Contributions
Developed for the Comp 479/6791 course at Concordia University, this project serves as a practical application of web crawling, data processing, and sentiment analysis techniques.

---

*Note: For detailed information on each script's functionality, refer to the in-line comments within the files.*