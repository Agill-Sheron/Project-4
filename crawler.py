import os
import requests
from bs4 import BeautifulSoup, SoupStrainer
from urllib.parse import urljoin
from robots import is_url_allowed
import time
from tqdm import tqdm

def crawl_website(start_url, max_urls=50, delay=1):
    visited_urls = set()
    urls_to_visit = [start_url]
    robots_url = "https://www.concordia.ca/robots.txt"
    html_dir = "./html"

    # Create the directory if it doesn't exist
    if not os.path.exists(html_dir):
        os.makedirs(html_dir)

    while urls_to_visit and len(visited_urls) < max_urls:
        current_url = urls_to_visit.pop(0)
        if current_url in visited_urls or not is_url_allowed(current_url, robots_url):
            continue

        try:
            response = requests.get(current_url, timeout=5)  # Timeout for the request
            soup = BeautifulSoup(response.text, 'html.parser')

            # Save the HTML content to a file
            html_file_path = os.path.join(html_dir, f"{len(visited_urls)}.html")
            with open(html_file_path, 'w', encoding='utf-8') as file:
                file.write(response.text)

            for link in soup.find_all('a', href=True):
                absolute_link = urljoin(current_url, link['href'])
                if absolute_link.startswith("https://www.concordia.ca") and absolute_link not in visited_urls:
                    urls_to_visit.append(absolute_link)

            visited_urls.add(current_url)
        except requests.exceptions.RequestException as e:
            print(f"Request failed for {current_url}: {e}")

        time.sleep(delay)  # Rate limiting

    return visited_urls

# Example usage
crawled_urls = crawl_website("https://www.concordia.ca", max_urls=100, delay=2)
print(f"Crawled {len(crawled_urls)} URLs")

def extract_text_from_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Remove script and style elements
    for script_or_style in soup(['script', 'style']):
        script_or_style.extract()

    # Get text
    text = soup.get_text()

    # Break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # Break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))

    # Drop blank lines and return clean text
    return '\n'.join(chunk for chunk in chunks if chunk)

def save_extracted_text(html_dir, parsed_dir):
    if not os.path.exists(parsed_dir):
        os.makedirs(parsed_dir)

    for filename in os.listdir(html_dir):
        html_file_path = os.path.join(html_dir, filename)
        parsed_file_path = os.path.join(parsed_dir, filename.replace('.html', '.txt'))

        with open(html_file_path, 'r', encoding='utf-8') as file:
            html_content = file.read()
            extracted_text = extract_text_from_html(html_content)

        with open(parsed_file_path, 'w', encoding='utf-8') as file:
            file.write(extracted_text)

# Directory paths
html_dir = './html'
parsed_dir = './parsed'

# Extract and save text
save_extracted_text(html_dir, parsed_dir)
