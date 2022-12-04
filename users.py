from flask import Flask, jsonify, request

app = Flask(__name__)

users = [
    {
        'id': 1,
        'name': 'Ricardo Oliveira',
        'mail': 'rbonilha@gmail.com',
        'address': {
            'street': 'Rua teste',
            'number': '456',
            'code': '01310100',
            'neighborhood': 'Bela Vista',
            'city': 'São Paulo',
            'stateCode': 'SP',
            'countryCode': 'BR'
        }
    },
]

# get all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

# get one user by id
@app.route('/users/<int:id>', methods=['GET'])
def get_user_by_id(id):
    for user in users:
        if user.get('id') == id:
            return jsonify(user)

# update one user by id
@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    changed_user = request.get_json()
    for index, user in enumerate(users):
        if user.get('id') == id:
            users[index].update(changed_user)
            return jsonify(users[index])

# create new user
@app.route('/users', methods=['POST'])
def create_user():
    new_user = request.get_json()
    new_user['id'] = users[-1]['id'] + 1
    users.append(new_user)
    return jsonify(users)

# delete user by id
@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    for index, user in enumerate(users):
        if user.get('id') == id:
            del users[index]
            return jsonify(users)

app.run(port=5000, host='localhost', debug=True)

