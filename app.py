from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

with open('house_price_model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    prediction = model.predict([[data['feature1'], data['feature2'], data['feature3']]])
    return jsonify({'prediction': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)
