from flask import Flask, request, jsonify
import pandas as pd
import joblib

app = Flask(__name__)

# Load the saved RandomForestRegressor model
rf_model = joblib.load('src/models/rf_model.pkl')

# Load the label encoders for categorical features
label_encoders = joblib.load('src/models/label_encoders.pkl')


@app.route('/predict', methods=['POST'])
def predict():
    # Get the JSON data from the request
    input_data = request.get_json()

    # Prepare the input data as a DataFrame
    input_df = pd.DataFrame([input_data])

    # Encode categorical features using the loaded label encoders
    for feature, encoder in label_encoders.items():
        input_df[feature] = encoder.transform(input_df[feature])

    # Make predictions using the loaded model
    predictions = rf_model.predict(input_df)

    # Format the predictions as a JSON response
    response = {'predictions': predictions.tolist()}

    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)
