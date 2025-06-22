import pandas as pd
from typing import List, Dict, Any
import re
from transformers import AutoTokenizer

# Load the Hugging Face tokenizer for XLM-Roberta (good for Amharic)
tokenizer = AutoTokenizer.from_pretrained("xlm-roberta-base")

# Common Amharic prepositions and function prefixes
AMHARIC_PREFIXES = [
    "በ", "ከ", "ለ", "የ"
]

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
    Cleans and normalizes a single Amharic message.
    """
    if not isinstance(text, str):
        return ""
    
    text = normalize_amharic(text)
    
    # Remove URLs
    text = re.sub(r'https?://\S+|www\.\S+', '', text)
    
    # Remove emojis and symbols (preserve Amharic and punctuation)
    text = re.sub(r'[^\u1200-\u137F\s0-9.,!?\'"፡።፣፤]', '', text)
    
    # Normalize whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text

def lemmatize_amharic(text: str) -> str:
    """
    Basic rule-based lemmatization for Amharic by removing common prefixes.
    Returns lemmatized text.
    """
    words = text.split()
    lemmatized_words = []

    for word in words:
        original = word
        for prefix in sorted(AMHARIC_PREFIXES, key=len, reverse=True):
            if word.startswith(prefix) and len(word) > len(prefix) + 1:
                word = word[len(prefix):]
                break  # Remove only one prefix
        lemmatized_words.append(word)

    return " ".join(lemmatized_words)

def tokenize(text: str) -> List[str]:
    """
    Tokenizes text using Hugging Face's XLM-Roberta tokenizer.
    """
    if not isinstance(text, str) or not text.strip():
        return []
    return tokenizer.tokenize(text)

def preprocess_text(text: str) -> Dict[str, Any]:
    """
    Applies cleaning, lemmatization, and tokenization.
    """
    cleaned = clean_text(text)
    lemmatized = lemmatize_amharic(cleaned)
    tokens = tokenize(lemmatized)
    return {
        "cleaned": lemmatized,
        "tokens": tokens
    }

def preprocess_dataframe(df: pd.DataFrame, text_col='Message') -> pd.DataFrame:
    """
    Preprocess the dataset: clean, lemmatize, tokenize.
    Adds 'cleaned_text' and 'tokens' columns.
    """
    processed = df[text_col].apply(preprocess_text)

    df['cleaned_text'] = processed.apply(lambda x: x['cleaned'])
    df['tokens'] = processed.apply(lambda x: x['tokens'])

    # Drop rows with no cleaned content
    df = df[df['cleaned_text'].str.strip().astype(bool)]

    return df
