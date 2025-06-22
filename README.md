# EthioMart NER Project

## Overview
The EthioMart NER Project aims to develop a Named Entity Recognition (NER) system tailored for extracting relevant information from messages scraped from Telegram. This project utilizes advanced language models to identify and classify entities within the text, providing valuable insights for vendor analytics.

## Project Structure
The project is organized into the following directories and files:

- **README.md**: Documentation for the project.
- **requirements.txt**: Lists the Python dependencies required for the project.
- **data/**: Contains various datasets.
  - **raw/**: Raw messages scraped from Telegram.
  - **processed/**: Preprocessed data (tokenized, cleaned).
  - **labeled_conll/**: CoNLL formatted labeled data for training and evaluation.
- **scripts/**: Contains scripts for data scraping, preprocessing, and analysis.
  - **telegram_scraper.py**: Script to scrape messages from Telegram using Telethon.
  - **preprocess.py**: Handles text normalization and tokenization.
  - **label_verifier.py**: Checks CoNLL labels for correctness.
  - **scorecard_engine.py**: Generates vendor analytics scoring.
- **models/**: Contains Jupyter notebooks for model training and saved model checkpoints.
  - **training_xlmroberta.ipynb**: Fine-tuning XLM-R model.
  - **training_afroxlmr.ipynb**: Fine-tuning AfroXLMR model.
  - **trained_models/**: Directory for saved model checkpoints.
- **interpretability/**: Contains notebooks and notes for model interpretability.
  - **shap_analysis.ipynb**: SHAP/LIME interpretability analysis scripts.
  - **difficult_cases.md**: Notes on model misclassifications.
- **notebooks/**: Contains exploratory data analysis notebooks.
  - **eda_preprocessing.ipynb**: Data exploration and preprocessing tests.
- **outputs/**: Contains output files for model performance and analytics.
  - **metrics_summary.csv**: Summary of model performance metrics.
  - **vendor_scorecard.csv**: Final scorecard table for vendor analytics.
- **reports/**: Contains interim and final reports.
  - **interim_summary.pdf**: Interim findings report.
  - **final_report_blog.pdf**: Final project overview report.

## Setup Instructions
1. Clone the repository:
   ```
   git clone https://github.com/ayanasamuel8/amharic-text-extractor.git
   ```
2. Navigate to the project directory:
   ```
   cd amharic-text-extractor
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage Guidelines
- Use the `telegram_scraper.py` script to collect raw messages from Telegram.
- Preprocess the collected data using `preprocess.py`.
- Train the models using the provided Jupyter notebooks in the `models/` directory.
- Evaluate model performance and generate analytics using the scripts in the `scripts/` directory.
- Review the interpretability analysis in the `interpretability/` directory to understand model decisions.

## Contribution
Contributions to the EthioMart NER Project are welcome. Please submit a pull request or open an issue for any suggestions or improvements.