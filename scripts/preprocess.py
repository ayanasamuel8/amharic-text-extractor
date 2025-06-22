import pandas as pd
import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('stopwords')

def load_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.readlines()

def clean_text(text):
    text = text.lower()  # Convert to lowercase
    text = re.sub(r'\d+', '', text)  # Remove numbers
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    return text

def tokenize_text(text):
    tokens = word_tokenize(text)
    return [token for token in tokens if token not in stopwords.words('amharic')]

def preprocess_data(raw_data):
    processed_data = []
    for line in raw_data:
        cleaned_line = clean_text(line)
        tokens = tokenize_text(cleaned_line)
        processed_data.append(tokens)
    return processed_data

if __name__ == "__main__":
    raw_file_path = 'data/raw/sample_data.txt'  # Update with actual raw data file path
    raw_data = load_data(raw_file_path)
    processed_data = preprocess_data(raw_data)
    
    # Save processed data to a file
    with open('data/processed/processed_data.txt', 'w', encoding='utf-8') as file:
        for tokens in processed_data:
            file.write(' '.join(tokens) + '\n')