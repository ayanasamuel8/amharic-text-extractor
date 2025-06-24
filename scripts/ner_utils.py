import pandas as pd
from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline, AutoConfig
import torch

# Define label mapping (you can move this to a shared config file if needed)
LABELS = ['O', 'B-PRODUCT', 'I-PRODUCT', 'B-PRICE', 'I-PRICE', 'B-LOC', 'I-LOC']
LABEL2ID = {label: i for i, label in enumerate(LABELS)}
ID2LABEL = {i: label for label, i in LABEL2ID.items()}

def load_ner_pipeline(model_path: str):
    """Load a fine-tuned NER model and tokenizer with correct label mappings."""
    device = 0 if torch.cuda.is_available() else -1

    config = AutoConfig.from_pretrained(
        model_path,
        id2label=ID2LABEL,
        label2id=LABEL2ID
    )
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = AutoModelForTokenClassification.from_pretrained(model_path, config=config)

    return pipeline("ner", model=model, tokenizer=tokenizer, grouped_entities=True, device=device)

def extract_entities_from_text(text: str, ner_pipeline) -> dict:
    """Extract price and product entities from text using the pipeline."""
    entities = ner_pipeline(str(text))
    prices, products = [], []
    for ent in entities:
        label = ent.get("entity_group") or ent.get("entity")
        if "PRICE" in label.upper():
            prices.append(ent["word"])
        elif "PRODUCT" in label.upper():
            products.append(ent["word"])
    return {
        "extracted_prices": ", ".join(prices) if prices else None,
        "extracted_products": ", ".join(products) if products else None,
    }

def enrich_dataframe_with_entities(df: pd.DataFrame, text_col: str, ner_pipeline) -> pd.DataFrame:
    """Add extracted entity columns to a DataFrame."""
    extracted = df[text_col].apply(lambda x: extract_entities_from_text(x, ner_pipeline))
    extracted_df = pd.DataFrame(list(extracted))
    return pd.concat([df, extracted_df], axis=1)
