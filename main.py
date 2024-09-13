import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from joblib import dump
import numpy as np

# Load the dataset
data = pd.read_csv('Housing.csv')

# Data Preprocessing
X = data[['area', 'bedrooms', 'bathrooms', 'stories', 'parking']]
y = data['price']

# Handling missing values (if any)
X.fillna(X.mean(), inplace=True)

# Splitting the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model Training
model = LinearRegression()
model.fit(X_train, y_train)

# Model Evaluation
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")

# Save the trained model
dump(model, 'house_price_model.joblib')
