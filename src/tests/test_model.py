import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import joblib
import os

def test_model_training():
    # Load the dataset
    diamonds_df = pd.read_csv(os.path.join(os.path.dirname(__file__), '..', 'data', 'diamonds.csv'))

    # Encode categorical variables using LabelEncoder
    label_encoders = {}
    for col in ['cut', 'color', 'clarity']:
        encoder = LabelEncoder()
        diamonds_df[col] = encoder.fit_transform(diamonds_df[col])
        label_encoders[col] = encoder

    # Split the data into features and target variable
    X = diamonds_df.drop(columns=['price'])
    y = diamonds_df['price']

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize and train the RandomForestRegressor model
    rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
    rf_model.fit(X_train, y_train)

    # Make predictions on the test set
    y_pred = rf_model.predict(X_test)

    # Check model performance metrics
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    # Assert that model performance metrics are within acceptable limits
    assert mse < 1000, "Mean Squared Error too high"
    assert r2 > 0.5, "R-squared too low"

def test_model_saving():
    # Load the trained model and label encoders
    rf_model = joblib.load(os.path.join(os.path.dirname(__file__), '..', 'models', 'rf_model.pkl'))
    label_encoders = joblib.load(os.path.join(os.path.dirname(__file__), '..', 'models', 'label_encoders.pkl'))

    # Perform assertions to check if the loaded model and encoders are valid
    assert isinstance(rf_model, RandomForestRegressor), "Invalid model loaded"
    assert isinstance(label_encoders, dict), "Invalid label encoders loaded"
