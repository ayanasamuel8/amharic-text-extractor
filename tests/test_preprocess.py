import unittest
import pandas as pd
from scripts.preprocess import clean_text, tokenize, preprocess_text, preprocess_dataframe

class TestPreprocessing(unittest.TestCase):

    def test_clean_text_removes_urls_and_symbols(self):
        text = "Check this out! https://example.com 😄 #ተማሪ"
        cleaned = clean_text(text)
        self.assertNotIn("https://", cleaned)
        self.assertNotIn("😄", cleaned)
        self.assertIn("ተማሪ", cleaned)

    def test_tokenize_works(self):
        text = "እንኳን ደህና መጣህ"
        tokens = tokenize(text)
        self.assertIsInstance(tokens, list)
        self.assertGreater(len(tokens), 0)
        self.assertTrue(all(isinstance(tok, str) for tok in tokens))

    def test_preprocess_text_structure(self):
        raw = "ልጅህን ከፍ አድርግ!"
        result = preprocess_text(raw)
        self.assertIn("cleaned", result)
        self.assertIn("tokens", result)
        self.assertIsInstance(result["tokens"], list)

    def test_preprocess_dataframe_output(self):
        data = {
            "Message": [
                "እንኳን ደህና መጣህ!",
                "Visit: http://google.com 🌍",
                "",
                None
            ]
        }
        df = pd.DataFrame(data)
        result_df = preprocess_dataframe(df)
        self.assertIn("cleaned_text", result_df.columns)
        self.assertIn("tokens", result_df.columns)
        self.assertTrue(all(isinstance(row, list) for row in result_df["tokens"]))
        self.assertGreater(len(result_df), 0)

if __name__ == "__main__":
    unittest.main()
