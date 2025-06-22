# Amharic Text Preprocessing and NER Labeling Pipeline

This project provides tools and scripts to preprocess Amharic text data, perform tokenization using Hugging Face's XLM-RoBERTa tokenizer, and label a subset of messages in CoNLL format for Named Entity Recognition (NER) tasks.

## Features

- **Text Normalization & Cleaning:**  
  Normalize Amharic punctuation and remove unwanted characters, URLs, and emojis.

- **Tokenization:**  
  Tokenize Amharic text using the pretrained XLM-RoBERTa tokenizer.

- **Lemmatization (optional):**  
  Support for Amharic lemmatization to improve entity labeling consistency.

- **NER Labeling:**  
  Label product, price, and location entities in Amharic messages in the CoNLL format.

## Directory Structure

```/
├── scripts/ # Preprocessing and tokenization scripts
├── data/raw # Raw datasets
├── data/processed #  processed datasets
├── data/labeled/ # Labeled data in CoNLL format
├── notebooks/ # Jupyter notebooks for exploration and annotation
├── tests/ # Unit tests for preprocessing functions
├── README.md # Project overview and instructions
```

## Getting Started

### Requirements

- Python 3.8+
- `transformers` library (for tokenizer)
- `pandas`

Install dependencies:

```bash
pip install -r requirements.txt
```
## Usage
### Preprocess data:

```python
from scripts.preprocess import preprocess_dataframe
import pandas as pd

df = pd.read_csv('path/to/your/csv_file')
processed_df = preprocess_dataframe(df, text_col='Message')
processed_df.to_csv('data/processed_messages.csv', index=False)
```
## Manual NER labeling:

Select a subset of preprocessed messages.

Label entities in CoNLL format following the guidelines:

B-Product, I-Product

B-PRICE, I-PRICE

B-LOC, I-LOC

O for tokens outside entities

Save labeled data:

Save the labeled data in plain text files (*.conll) inside the data/labeled_conll/ directory.

CoNLL Labeling Format
Each token is on its own line followed by the entity label, separated by a space:

```mathematica
token B-Product
token I-Product
token O

token B-LOC
token I-LOC
token O
```
Sentences/messages are separated by blank lines.

## Contributing
Feel free to open issues or submit pull requests to improve the preprocessing, tokenization, or labeling process.

This project is for Amharic text preprocessing and NER annotation purposes. and we'll be updated as project grows.