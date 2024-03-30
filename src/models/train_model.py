import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import joblib

# Assuming the dataset is stored in a CSV file named 'diamonds.csv'
diamonds_df = pd.read_csv('../data/diamonds.csv')

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

# Standardize the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Initialize and train the RandomForestRegressor model
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
rf_model.fit(X_train_scaled, y_train)

# Make predictions on the test set
y_pred = rf_model.predict(X_test_scaled)

# Calculate evaluation metrics (e.g., Mean Squared Error and R-squared)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Save the trained model and label encoders
joblib.dump(rf_model, 'rf_model.pkl')
joblib.dump(label_encoders, 'label_encoders.pkl')

print(f'Mean Squared Error: {mse}')
print(f'R-squared: {r2}')
