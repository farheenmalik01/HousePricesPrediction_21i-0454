import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from joblib import dump
import numpy as np

def load_and_preprocess_data(filepath):
    # Load the dataset
    data = pd.read_csv(filepath)
    
    # Data Preprocessing
    # Selecting relevant features
    X = data[['area', 'bedrooms', 'bathrooms', 'stories', 'parking']]
    y = data['price']
    
    # Handling missing values (if any)
    X = X.fillna(X.mean())
    
    # Feature Scaling
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # Splitting the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
    
    return X_train, X_test, y_train, y_test

def train_model(X_train, y_train):
    # Create a pipeline
    pipeline = Pipeline(steps=[('scaler', StandardScaler()), ('model', LinearRegression())])
    
    # Fitting the model
    pipeline.fit(X_train, y_train)
    
    return pipeline

def main():
    # Path to dataset
    filepath = 'Housing.csv'
    
    # Load and preprocess data
    X_train, X_test, y_train, y_test = load_and_preprocess_data(filepath)
    
    # Train the model
    pipeline = train_model(X_train, y_train)
    
    # Model Evaluation
    y_pred = pipeline.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    print(f"Mean Squared Error: {mse}")
    
    # Save the model
    dump(pipeline, 'house_price_model.joblib')
    print("Model trained and saved successfully!")

if __name__ == '__main__':
    main()
