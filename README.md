# 📚 Amharic NER Pipeline for EthioMart

This repository contains tools and scripts to preprocess Amharic Telegram text data, perform Named Entity Recognition (NER) using a fine-tuned transformer model, and extract vendor analytics for micro-lending evaluation.

---

## ✨ Features

- **✅ Text Cleaning & Normalization**
  - Removes emojis, symbols, links, and redundant punctuation.
  - Normalizes Amharic-specific characters and spacing.

- **🔠 Tokenization**
  - Uses `XLM-RoBERTa` tokenizer for multilingual support.
  - Token-level formatting for CoNLL-style entity tagging.

- **🏷️ NER Annotation Support**
  - Manual annotation via CoNLL format.
  - Supports entity labels:
    - `B-PRICE`, `I-PRICE`
    - `B-PRODUCT`, `I-PRODUCT`
    - `B-LOC`, `I-LOC`
    - `O` for non-entity tokens

- **🧠 Model Fine-tuning**
  - Fine-tunes `xlm-roberta-base` on Amharic NER data.
  - Built using Hugging Face Transformers.

- **📊 Vendor Analytics & Scorecard**
  - Extracts product/price entities from vendor posts.
  - Computes posting frequency, engagement metrics, and Lending Score.

---

## 🗂️ Project Structure
``` yaml
/
├── scripts/
│ ├── preprocess.py # Cleaning and tokenization
│ ├── ner_utils.py # Entity extraction utilities
│ ├── vendor_metrics.py # Scorecard computation
│ └── telegram_scraper.py # Telegram data scraping
│
├── data/
│ ├── raw/ # Raw Telegram data
│ ├── processed/ # Cleaned + enriched data
│ └── labeled_conll/ # CoNLL annotated data
│
├── models/
│ └── trained_models/ # Fine-tuned XLM-RoBERTa model
│
├── notebooks/
│ ├── 01_preprocessing.ipynb
│ ├── 03_fine_tuning.ipynb
│ ├── 05_lime_and_shap.ipynb
│ └── 08_scorecard_analysis.ipynb
│
├── interpretability/
│ └── difficult_cases.md # Model errors & discussion
│
├── outputs/
│ └── enriched_data.csv # Product/price enriched records
│
├── tests/
│ ├── test_preprocess.py
│ └── test_dummy.py
│
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

### 📦 Installation

```bash
git clone https://github.com/yourname/ethiomart-ner.git
cd ethiomart-ner
pip install -r requirements.txt
```
## 🧹 Step 1: Preprocessing
```python
from scripts.preprocess import preprocess_dataframe
import pandas as pd

df = pd.read_csv("data/raw/telegram_data.csv")
cleaned_df = preprocess_dataframe(df, text_col="Message")
cleaned_df.to_csv("data/processed/cleaned_messages.csv", index=False)
```
## ✍️ Step 2: Manual NER Labeling
Use a subset of cleaned messages.

Annotate each token in CoNLL format:

```css
ስልክ  B-PRODUCT
በ    O
2000 B-PRICE
ብር   I-PRICE
```
Save labeled data in data/labeled_conll/ with blank lines between sentences.

## 🧠 Step 3: Model Training
Run training via notebook:

```bash
notebooks/03_fine_tuning.ipynb
```
### Model output saved to:

```bash
models/trained_models/
```
## 🔎 Step 4: Entity Extraction
Use the fine-tuned model to extract product and price entities:

```python
from scripts.ner_utils import load_ner_pipeline, enrich_dataframe_with_entities
import pandas as pd

df = pd.read_csv("data/processed/cleaned_messages.csv")
ner_pipe = load_ner_pipeline("models/trained_models/")
df_enriched = enrich_dataframe_with_entities(df, text_col="cleaned_text", ner_pipeline=ner_pipe)
df_enriched.to_csv("outputs/enriched_data.csv", index=False)
```
## 📊 Step 5: Vendor Scorecard
Generate vendor-level analytics and a Lending Score:

```python
from scripts.vendor_metrics import prepare_prices, compute_vendor_metrics

df = pd.read_csv("outputs/enriched_data.csv")
df = prepare_prices(df)
scorecard_df = compute_vendor_metrics(df)
scorecard_df.to_csv("outputs/vendor_scorecard.csv", index=False)
```
## ✅ Tests
```bash
pytest
```
## Covers:

### Preprocessing and normalization

### Entity extraction logic

# 📌 Contributing
We welcome contributions that:

- Improve preprocessing for Amharic

- Add more entity classes

- Enhance analytics (e.g., customer sentiment, time series trends)

1. Fork the repo

2. Create your feature branch (git checkout -b feature/amharic-cleaner)

3. Commit your changes

4. Open a pull request

# 🧭 Future Roadmap
- ✅ Live Telegram feed scoring

- 🚧 Expand labeled dataset size

- 🚧 Add dashboard for scorecard insights

- 🚧 Support other Ethiopian languages (e.g., Afaan Oromoo)

# 📜 License

MIT License – open-source and community-friendly!

EthioMart NLP | Powered by XLM-R and Open Source Intelligence 🇪🇹