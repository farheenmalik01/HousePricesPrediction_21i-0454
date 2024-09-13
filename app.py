from flask import Flask, request, jsonify, render_template
from flask import render_template
from joblib import load
import numpy as np

app = Flask(__name__)

pipeline = load('house_price_model.joblib')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

        area = float(data.get('area', 0))
        bedrooms = int(data.get('bedrooms', 0))
        bathrooms = int(data.get('bathrooms', 0))
        stories = int(data.get('stories', 0))
        parking = int(data.get('parking', 0))
        
        # Handle categorical features as binary
        mainroad = int(data.get('mainroad', 0))
        guestroom = int(data.get('guestroom', 0))
        basement = int(data.get('basement', 0))
        hotwaterheating = int(data.get('hotwaterheating', 0))
        airconditioning = int(data.get('airconditioning', 0))
        prefarea = int(data.get('prefarea', 0))

        # Create a numpy array with the features in the order the model expects
        input_features = np.array([[area, bedrooms, bathrooms, stories, mainroad, guestroom, basement, hotwaterheating, airconditioning, parking, prefarea]])
        
        prediction = pipeline.predict(input_features)
        return jsonify({'predicted_price': prediction[0]})
    
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
