import unittest
from main import load_and_preprocess_data, train_model
from joblib import load

class TestHousePriceModel(unittest.TestCase):
    def test_load_and_preprocess_data(self):
        # Assuming the dataset file is in the current directory
        X_train, X_test, y_train, y_test = load_and_preprocess_data('Housing.csv')
        self.assertGreater(len(X_train), 0, "Training data should not be empty")
        self.assertGreater(len(y_train), 0, "Training labels should not be empty")
        self.assertEqual(X_train.shape[1], 5, "There should be 5 features")

    def test_train_model(self):
        # Load and preprocess data
        X_train, X_test, y_train, y_test = load_and_preprocess_data('Housing.csv')
        
        # Train the model
        pipeline = train_model(X_train, y_train)
        
        # Check if the pipeline is not None
        self.assertIsNotNone(pipeline, "Pipeline should not be None after training")

        # Test the model's prediction
        y_pred = pipeline.predict(X_test)
        self.assertEqual(len(y_pred), len(y_test), "Number of predictions should match number of test samples")

if __name__ == '__main__':
    unittest.main()
