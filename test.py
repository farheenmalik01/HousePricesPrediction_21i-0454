import unittest
from main import load_and_preprocess_data, train_model
import pandas as pd

class TestHousePriceModel(unittest.TestCase):
    def test_load_and_preprocess_data(self):
        X_train, X_test, y_train, y_test = load_and_preprocess_data('data/Housing.csv')
        self.assertGreater(len(X_train), 0)
        self.assertGreater(len(y_train), 0)

    def test_train_model(self):
        X_train, X_test, y_train, y_test = load_and_preprocess_data('data/Housing.csv')
        model = train_model(X_train, y_train)
        self.assertIsNotNone(model)

if __name__ == '__main__':
    unittest.main()
