import os
from bs4 import BeautifulSoup

def start_parsing(html_dir, parsed_dir):
    if not os.path.exists(parsed_dir):
        os.makedirs(parsed_dir)

    for html_filename in os.listdir(html_dir):
        html_file_path = os.path.join(html_dir, html_filename)
        parsed_file_path = os.path.join(parsed_dir, html_filename.replace('.html', '.txt'))

        with open(html_file_path, 'r', encoding='utf-8') as file:
            html_content = file.read()
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
            text = '\n'.join(chunk for chunk in chunks if chunk)
        
        with open(parsed_file_path, 'w', encoding='utf-8') as file:
            file.write(text)
