import os
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# NLTK Stop words
stop_words = set(stopwords.words('english'))

# Adding custom stop words
custom_stop_words = ['concordia', 'school', 'university', 'student', 'students']
stop_words.update(custom_stop_words)

# Preprocessing function
def preprocess_text(text):
    lemmatizer = WordNetLemmatizer()
    
    # Tokenization
    tokens = word_tokenize(text)
    
    # Removing stop words and lemmatization
    preprocessed_text = ' '.join([lemmatizer.lemmatize(word.lower()) for word in tokens if word.isalpha() and word.lower() not in stop_words])
    
    return preprocessed_text

# Read, preprocess, and save the text
def preprocess_and_save_files(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        with open(os.path.join(input_dir, filename), 'r', encoding='utf-8') as file:
            text = file.read()
            preprocessed_text = preprocess_text(text)

        with open(os.path.join(output_dir, filename), 'w', encoding='utf-8') as file:
            file.write(preprocessed_text)

# Directory paths
parsed_dir = './parsed'
preprocessed_dir = './preprocessed'

# Process and save files
preprocess_and_save_files(parsed_dir, preprocessed_dir)
