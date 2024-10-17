import unittest
import pandas as pd
from data_cleaning import clean_data

class TestCleaning(unittest.TestCase):
    def setUp(self):
        # Prepare test raw data
        self.raw_data = {'date': ['2024-10-12', '2024-10-13', '2024-10-13'],
                         'text': ['Sample message 1', 'Sample message 2', None]}
        self.raw_df = pd.DataFrame(self.raw_data)
        self.raw_df.to_csv('data/raw/test_raw_data.csv', index=False)

    def test_clean_data(self):
        # Run the cleaning script
        clean_data('data/raw/test_raw_data.csv')
        cleaned_df = pd.read_csv('data/cleaned/cleaned_data.csv')

        # Check for duplicates removal
        self.assertEqual(len(cleaned_df), 2, "Duplicate records not removed")

        # Check for missing values handling
        self.assertFalse(cleaned_df['text'].isnull().any(), "Missing values not handled")

    def tearDown(self):
        # Clean up test files after running the tests
        import os
        os.remove('data/raw/test_raw_data.csv')
        os.remove('data/cleaned/cleaned_data.csv')

if __name__ == '__main__':
    unittest.main()
