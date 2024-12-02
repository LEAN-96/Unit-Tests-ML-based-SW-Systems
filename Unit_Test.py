import unittest
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import pandas as pd
from Unit_TheAlgorithm import CustomLogisticRegression

class TestLogisticRegression(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Set up the test dataset and model."""
        # Load dataset
        data = pd.read_csv('data/Advertising.csv')
        X = data[['Daily Time Spent on Site', 'Age', 'Area Income', 'Daily Internet Usage', 'Male']]
        y = data['Clicked on Ad']

        # Split data
        cls.X_train, cls.X_test, cls.y_train, cls.y_test = train_test_split(X, y, test_size=0.3, random_state=42)
        cls.model = CustomLogisticRegression()

    def test_fit_runtime(self):
        """Test that the fit function runs within acceptable runtime."""
        import time
        start_time = time.time()
        self.model.fit(self.X_train, self.y_train)
        baseline_runtime = time.time() - start_time

        # Validate runtime
        start_time = time.time()
        self.model.fit(self.X_train, self.y_train)
        runtime = time.time() - start_time
        self.assertLessEqual(runtime, 1.2 * baseline_runtime, "Fit runtime exceeded limits.")

    def test_predict_accuracy(self):
        """Test prediction accuracy of the model."""
        self.model.fit(self.X_train, self.y_train)
        predictions = self.model.predict(self.X_test)

        accuracy = accuracy_score(self.y_test, predictions)
        self.assertGreaterEqual(accuracy, 0.8, "Prediction accuracy is below threshold.")

if __name__ == "__main__":
    unittest.main()
