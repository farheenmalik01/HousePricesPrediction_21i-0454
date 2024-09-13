import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import pickle

def load_and_preprocess_data(file_path):
    data = pd.read_csv(file_path)
    X = data[['area', 'bedrooms', 'bathrooms', 'stories', 'mainroad', 'guestroom', 'basement', 'hotwaterheating', 'airconditioning', 'parking', 'prefarea']]
    y = data['price']

    X = pd.get_dummies(X, drop_first=True)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test

def train_model(X_train, y_train):
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    return model

def save_model(model, filename):
    with open(filename, 'wb') as file:
        pickle.dump(model, file)

if __name__ == "__main__":
    X_train, X_test, y_train, y_test = load_and_preprocess_data('data/Housing.csv')
    model = train_model(X_train, y_train)
    save_model(model, 'house_price_model.pkl')
    print("Model trained and saved successfully.")