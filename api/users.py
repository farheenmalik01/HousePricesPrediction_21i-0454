
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/users', methods=['GET'])
def get_users():
    return jsonify({'message': 'List of users'})

@app.route('/api/users/<int:id>', methods=['GET'])
def get_user(id):
    return jsonify({'message': f'Details of user with ID {id}'})

@app.route('/api/users', methods=['POST'])
def create_user():
    return jsonify({'message': 'User created'})

@app.route('/api/users/<int:id>', methods=['PUT'])
def update_user(id):
    return jsonify({'message': f'User with ID {id} updated'})

@app.route('/api/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    return jsonify({'message': f'User with ID {id} deleted'})

if __name__ == '__main__':
    app.run(debug=True)
