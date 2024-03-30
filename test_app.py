import unittest
import json
from app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_predict_endpoint(self):
        # Prepare a sample input data for prediction
        input_data = {
            "carat": 0.23,
            "cut": "Ideal",
            "color": "E",
            "clarity": "SI2",
            "depth": 61.5,
            "table": 55,
            "x": 3.95,
            "y": 3.98,
            "z": 2.43,
            "price": 0
        }

        # Make a POST request to the /predict endpoint with the sample input data
        response = self.app.post('/predict', json=input_data)
        
        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Decode the response data from JSON format
        data = json.loads(response.data.decode('utf-8'))

        # Check if the response contains the 'predictions' key
        self.assertIn('predictions', data)

        # Check if the predictions are a list of floats
        predictions = data['predictions']
        self.assertIsInstance(predictions, list)
        for pred in predictions:
            self.assertIsInstance(pred, float)

if __name__ == '__main__':
    unittest.main()
