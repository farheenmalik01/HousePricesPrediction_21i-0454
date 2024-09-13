from flask import Flask, request, jsonify
from joblib import load
import numpy as np

app = Flask(__name__)

# Load the trained model
model = load('house_price_model.joblib')

@app.route('/')
def index():
    return "House Price Prediction API is running. Use the /predict endpoint to make predictions."

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        area = float(data['area'])
        bedrooms = int(data['bedrooms'])
        bathrooms = int(data['bathrooms'])
        stories = int(data['stories'])
        parking = int(data['parking'])

        # Validate input data
        input_features = np.array([[area, bedrooms, bathrooms, stories, parking]])
        prediction = model.predict(input_features)
        
        return jsonify({'predicted_price': prediction[0]})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
