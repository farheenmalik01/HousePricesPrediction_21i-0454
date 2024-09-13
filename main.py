import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from joblib import dump
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression

def load_and_preprocess_data(file_path):
    data = pd.read_csv(file_path)
    X = data[['area', 'bedrooms', 'bathrooms', 'stories', 'mainroad', 'guestroom', 'basement', 'hotwaterheating', 'airconditioning', 'parking', 'prefarea']]
    y = data['price']

    X = pd.get_dummies(X, drop_first=True)

    X = X.fillna(X.mean())
    
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
    
    return X_train, X_test, y_train, y_test


def train_model(X_train, y_train):
    pipeline = Pipeline(steps=[('scaler', StandardScaler()), ('model', LinearRegression())])
    pipeline.fit(X_train, y_train)
    return pipeline

def main():
    filepath = 'Housing.csv'
    
    X_train, X_test, y_train, y_test = load_and_preprocess_data(filepath)
    
    pipeline = train_model(X_train, y_train)
    
    y_pred = pipeline.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    print(f"Mean Squared Error: {mse}")
    
    dump(pipeline, 'house_price_model.joblib')
    print("Model trained and saved successfully!")

if __name__ == '__main__':
    main()