from flask import Flask, request, jsonify
from flask import render_template
import pickle
import pandas as pd

app = Flask(__name__)

with open('house_price_model.pkl', 'rb') as file:
    model = pickle.load(file)

def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json(force=True)
        df = pd.DataFrame(data, index=[0])

        expected_columns = ['area', 'bedrooms', 'bathrooms', 'stories', 'mainroad_yes', 'guestroom_yes', 
                            'basement_yes', 'hotwaterheating_yes', 'airconditioning_yes', 'parking', 'prefarea_yes']
        for col in expected_columns:
            if col not in df.columns:
                df[col] = 0
        
        prediction = model.predict(df[expected_columns])[0]
        return jsonify({'predicted_price': prediction})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
