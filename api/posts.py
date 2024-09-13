
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/posts', methods=['GET'])
def get_posts():
    return jsonify({'message': 'List of posts'})

@app.route('/api/posts/<int:id>', methods=['GET'])
def get_post(id):
    return jsonify({'message': f'Details of post with ID {id}'})

@app.route('/api/posts', methods=['POST'])
def create_post():
    return jsonify({'message': 'Post created'})

@app.route('/api/posts/<int:id>', methods=['PUT'])
def update_post(id):
    return jsonify({'message': f'Post with ID {id} updated'})

@app.route('/api/posts/<int:id>', methods=['DELETE'])
def delete_post(id):
    return jsonify({'message': f'Post with ID {id} deleted'})

if __name__ == '__main__':
    app.run(debug=True)
