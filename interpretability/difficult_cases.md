# Difficult Cases in EthioMart NER Project

This document outlines the difficult cases encountered during the evaluation of the Named Entity Recognition (NER) models in the EthioMart project. It includes examples of misclassifications and challenges faced in accurately labeling entities.

## 1. Ambiguous Tokens
Certain words can appear in different contexts with different meanings. For example:

> _“ብር ወደ ባንክ ተቀበሉ”_ ("The birr was received at the bank.")

- The word **"ብር"** could be misclassified as a PRICE entity, even when it simply refers to the currency in a non-price context.

## 2. Overlapping or Nested Entities
Some sentences contain multiple entity types within close proximity or even overlapping:

> _“አዲስ መኪና በ200,000 ብር ተገዛ”_ ("A new car was bought for 200,000 birr")

- Here, **"መኪና"** should be labeled as PRODUCT and **"200,000 ብር"** as PRICE.
- The model may struggle to correctly segment and classify both entities simultaneously.

## 3. Unseen Synonyms or Domain Shifts
Tokens that were not present in the training data may be misclassified:

> For instance, **"ተሽከርካሪ"** (another word for car) may not be recognized as a PRODUCT.

- This is due to limited vocabulary exposure during training, especially in low-resource languages like Amharic.

## 4. Contextual Dependency Confusion
The model may fail in long or complex sentences where the dependency between tokens stretches across multiple words:

> _“በ100 ብር የተገዛ መጽሐፍ”_ ("The book that was bought for 100 birr")

- The model might misclassify **"100"** or **"መጽሐፍ"** if contextual linking is weak or truncated.

## 5. Tokenization Issues
Subword tokenization (e.g., WordPiece or SentencePiece) can break words into partial tokens:

> Example: “በ300” → "▁በ", "300"

- If the tokenizer splits an important token awkwardly, it may affect the model's labeling accuracy.

---