# Web Crawling and Sentiment Analysis Project

## Project Overview
This project aims to crawl the Concordia University website, process the extracted text data, perform document clustering, and conduct sentiment analysis on the clustered documents. It showcases an end-to-end pipeline from data collection to analysis, adhering to ethical web scraping guidelines.

## Setup and Installation
Before running the project, ensure you have Python installed along with the following libraries:
- Scrapy
- BeautifulSoup
- NLTK
- scikit-learn
- Afinn
- NumPy
- tqdm

You can install these packages using pip:
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
- `main.py`: Orchestrates the entire crawling, processing, and analysis pipeline.
- `scrapy_spider.py`: Defines the Scrapy spider for web crawling.

## Running the Project
To run the project, execute the `main.py` script:
```bash
python main.py
```
This will sequentially execute the processes defined in each script, with progress tracked via a tqdm progress bar.

## Outputs
The project generates several outputs:
- Crawled HTML files from the Concordia website.
- Parsed and preprocessed text data.
- TF-IDF matrix and feature names.
- Cluster labels and top terms for each cluster.
- Sentiment scores for each cluster.

## Ethical Considerations
This project strictly adheres to the web scraping guidelines provided by Concordia University's `robots.txt` file. The `robots.py` script ensures that the crawler respects these guidelines, promoting ethical data collection practices.

## Contributions
This project was developed as part of the Comp 479/6791 course at Concordia University. It serves as a practical implementation of web crawling, data processing, and sentiment analysis techniques.

---

*Note: This README provides an overview of the project's purpose, setup, and execution. For more detailed information on each script and their functionalities, refer to the in-line comments within each file.*