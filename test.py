import unittest
from main import load_and_preprocess_data, train_model
import pandas as pd
import os

class TestHousePriceModel(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.file_path = 'Housing.csv'
        # Ensure that the dataset file is in the correct location for the tests
        if not os.path.isfile(cls.file_path):
            raise FileNotFoundError(f"Test file {cls.file_path} not found.")

    def test_load_and_preprocess_data(self):
        X_train, X_test, y_train, y_test = load_and_preprocess_data(self.file_path)
        self.assertGreater(len(X_train), 0, "Training set should not be empty")
        self.assertGreater(len(y_train), 0, "Training labels should not be empty")
        self.assertGreater(len(X_test), 0, "Test set should not be empty")
        self.assertGreater(len(y_test), 0, "Test labels should not be empty")

    def test_train_model(self):
        X_train, X_test, y_train, y_test = load_and_preprocess_data(self.file_path)
        model = train_model(X_train, y_train)
        self.assertIsNotNone(model, "Model should not be None")

if __name__ == '__main__':
    unittest.main()
