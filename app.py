from flask import Flask, request, jsonify, render_template
from joblib import load
import numpy as np

app = Flask(__name__)

# Load the trained model pipeline
pipeline = load('house_price_model.joblib')

@app.route('/')
def index():
    # Render the HTML template for the user interface
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the JSON data from the request
        data = request.get_json()

        # Extracting input features and converting to appropriate types
        area = float(data['area'])
        bedrooms = int(data['bedrooms'])
        bathrooms = int(data['bathrooms'])
        stories = int(data['stories'])
        parking = int(data['parking'])

        # Preparing the input features for the model
        input_features = np.array([[area, bedrooms, bathrooms, stories, parking]])

        # Using the pipeline to make predictions
        prediction = pipeline.predict(input_features)
        
        # Return the predicted price as a JSON response
        return jsonify({'predicted_price': prediction[0]})

    except Exception as e:
        # Handle errors and return them as JSON response
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    # Start the Flask application in debug mode
    app.run(debug=True)
