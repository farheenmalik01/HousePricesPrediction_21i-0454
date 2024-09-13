import unittest
from main import preprocess_data, train_model
import pandas as pd

class TestModel(unittest.TestCase):

    def test_preprocess_data(self):
        data = pd.DataFrame({
            'feature1': [1, 2, 3],
            'feature2': [4, 5, 6],
            'feature3': [7, 8, 9],
            'price': [10, 12, 15]
        })
        X_train, X_test, y_train, y_test = preprocess_data(data)
        self.assertEqual(len(X_train), 2)
        self.assertEqual(len(y_train), 2)

    def test_train_model(self):
        X_train = [[1, 2, 3], [4, 5, 6]]
        y_train = [10, 20]
        model = train_model(X_train, y_train)
        self.assertIsNotNone(model)

if __name__ == '__main__':
    unittest.main()
