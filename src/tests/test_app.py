import pytest
from flask import Flask, request, jsonify
from src.app.app import app as flask_app
import os

@pytest.fixture
def client():
    # Create a test client using the Flask application
    with flask_app.test_client() as client:
        yield client

def test_predict_endpoint(client):
    # Prepare test data for prediction
    input_data = {
        "carat": 1.0,
        "cut": "Ideal",
        "color": "E",
        "clarity": "SI2",
        "depth": 61.5,
        "table": 55.0,
        "x": 3.95,
        "y": 3.98,
        "z": 2.43,
        "price": 0
    }

    # Send a POST request to the /predict endpoint
    response = client.post('/predict', json=input_data)

    # Check the response status code and data format
    assert response.status_code == 200, "Prediction request failed"
    assert 'predictions' in response.json, "Missing predictions in response"
    assert isinstance(response.json['predictions'], list), "Invalid predictions format"
