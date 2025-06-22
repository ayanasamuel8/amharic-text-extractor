import pandas as pd
from typing import List, Dict, Any
import re
from transformers import AutoTokenizer

# Load the Hugging Face tokenizer for XLM-Roberta (good for Amharic)
tokenizer = AutoTokenizer.from_pretrained("xlm-roberta-base")

def normalize_amharic(text: str) -> str:
    """
    Normalize Amharic-specific punctuation and spacing.
    """
    if not isinstance(text, str):
        return ""
    
    # Normalize special punctuation marks
    text = text.replace('\u1361', ' ')  # ፡ to space
    text = re.sub(r'[።፣፤]', '.', text)  # Sentence punctuation → period
    
    return text

def clean_text(text: str) -> str:
    """
    Cleans and normalizes a single Amharic message:
    - Removes URLs
    - Removes emojis/special symbols
    - Keeps Amharic, digits, and basic punctuation
    - Normalizes whitespace
    """
    if not isinstance(text, str):
        return ""
    
    text = normalize_amharic(text)
    
    # Remove URLs
    text = re.sub(r'https?://\S+|www\.\S+', '', text)
    
    # Remove emojis and symbols (keep Amharic block + basic punctuation + numbers)
    # Amharic Unicode block: 1200–137F
    text = re.sub(r'[^\u1200-\u137F\s0-9.,!?\'"፡።፣፤]', '', text)
    
    # Replace multiple whitespace characters with a single space
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text 

def tokenize(text: str) -> List[str]:
    """
    Tokenizes text using Hugging Face's XLM-Roberta tokenizer.
    Returns a list of subword tokens.
    """
    if not isinstance(text, str) or not text.strip():
        return []
    return tokenizer.tokenize(text)

def preprocess_text(text: str) -> Dict[str, Any]:
    """
    Applies cleaning and Hugging Face tokenization to a single text input.
    Returns a dictionary with cleaned text and token list.
    """
    cleaned = clean_text(text)
    tokens = tokenize(cleaned)
    return {
        "cleaned": cleaned,
        "tokens": tokens
    }

def preprocess_dataframe(df: pd.DataFrame, text_col='Message') -> pd.DataFrame:
    """
    Applies the preprocessing pipeline (clean + tokenize) to a DataFrame.
    Adds two new columns: 'cleaned_text', 'tokens'.
    Filters out rows with empty cleaned text.
    """
    processed = df[text_col].apply(preprocess_text)
    
    df['cleaned_text'] = processed.apply(lambda x: x['cleaned'])
    df['tokens'] = processed.apply(lambda x: x['tokens'])
    
    # Remove empty cleaned messages
    df = df[df['cleaned_text'].str.strip().astype(bool)]
    
    return df
