from flask import Flask, request, jsonify, g
from flask_cors import CORS
import bcrypt
from controllers.sale_controller import SaleController
from controllers.category_controller import CategoryController
from controllers.media_controller import MediaController
from controllers.user_controller import UserController
from controllers.user_group_controller import UserGroupController
from dao.sale_dao import SaleDAO
from dao.user_dao import UserDAO
import os
import logging

app = Flask(__name__)
CORS(app)  # Enable CORS

sale_dao = SaleDAO()
sale_controller = SaleController(sale_dao)
category_controller = CategoryController()
media_controller = MediaController()
user_controller = UserController()
user_group_controller = UserGroupController()
user_dao = UserDAO()

logging.basicConfig(level=logging.DEBUG if os.getenv('FLASK_ENV') == 'development' else logging.INFO)
logger = logging.getLogger(__name__)

# Middleware to check authentication
def authenticate(f):
    def wrapper(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'message': 'Unauthorized'}), 401
        # Here you can add your token validation logic
        # For simplicity, we assume the token is valid if it equals 'valid-token'
        if token != 'valid-token':
            return jsonify({'message': 'Unauthorized'}), 401
        return f(*args, **kwargs)
    wrapper.__name__ = f.__name__
    return wrapper

@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.json
        username = data['username']
        password = data['password']
        user = user_dao.get_user_by_username(username)

        # Debugging information for development
        if os.getenv('FLASK_ENV') == 'development':
            logger.debug(f"Debugging Info: Username: {username}, Password: {password}")

        if user:
            logger.debug(f"User found: {user}")
        else:
            logger.debug("User not found")

        if user and bcrypt.checkpw(password.encode('utf-8'), user['password'].encode('utf-8')):
            # Return a token for simplicity
            return jsonify({'message': 'Login successful!', 'user_level': user['user_level'], 'token': 'valid-token'})
        else:
            logger.debug("Password verification failed")
        return jsonify({'message': 'Invalid credentials!'}), 401
    except Exception as e:
        logger.error(f"Error during login: {e}")
        return jsonify({'message': 'An error occurred during login', 'error': str(e)}), 500

@app.route('/dashboard', methods=['GET'])
@authenticate
def dashboard():
    return jsonify({'message': 'Welcome to the dashboard!'})

@app.route('/sales', methods=['GET'])
@authenticate
def list_sales():
    sales = sale_controller.get_all_sales()
    return jsonify(sales)

@app.route('/sales', methods=['POST'])
@authenticate
def add_sale():
    data = request.json
    sale_controller.create_sale(data['product_id'], data['qty'], data['price'], data['date'])
    return jsonify({'message': 'Sale added successfully!'})

@app.route('/sales/<int:sale_id>', methods=['PUT'])
@authenticate
def update_sale(sale_id):
    data = request.json
    sale_controller.update_sale(sale_id, data['product_id'], data['qty'], data['price'], data['date'])
    return jsonify({'message': 'Sale updated successfully!'})

@app.route('/sales/<int:sale_id>', methods=['DELETE'])
@authenticate
def delete_sale(sale_id):
    sale_controller.remove_sale(sale_id)
    return jsonify({'message': 'Sale deleted successfully!'})

@app.route('/categories', methods=['GET'])
@authenticate
def list_categories():
    categories = category_controller.get_all_categories()
    return jsonify(categories)

@app.route('/categories', methods=['POST'])
@authenticate
def add_category():
    data = request.json
    category_controller.create_category(data['name'])
    return jsonify({'message': 'Category added successfully!'})

@app.route('/categories/<int:category_id>', methods=['PUT'])
@authenticate
def update_category(category_id):
    data = request.json
    category_controller.update_category(category_id, data['name'])
    return jsonify({'message': 'Category updated successfully!'})

@app.route('/categories/<int:category_id>', methods=['DELETE'])
@authenticate
def delete_category(category_id):
    category_controller.remove_category(category_id)
    return jsonify({'message': 'Category deleted successfully!'})

@app.route('/media', methods=['GET'])
@authenticate
def list_media():
    media = media_controller.get_all_media()
    return jsonify(media)

@app.route('/media', methods=['POST'])
@authenticate
def add_media():
    data = request.json
    media_controller.create_media(data['name'], data['type'], data['url'])
    return jsonify({'message': 'Media added successfully!'})

@app.route('/media/<int:media_id>', methods=['PUT'])
@authenticate
def update_media(media_id):
    data = request.json
    media_controller.update_media(media_id, data['name'], data['type'], data['url'])
    return jsonify({'message': 'Media updated successfully!'})

@app.route('/media/<int:media_id>', methods=['DELETE'])
@authenticate
def delete_media(media_id):
    media_controller.remove_media(media_id)
    return jsonify({'message': 'Media deleted successfully!'})

@app.route('/users', methods=['GET'])
@authenticate
def list_users():
    users = user_controller.get_all_users()
    return jsonify(users)

@app.route('/users', methods=['POST'])
@authenticate
def add_user():
    data = request.json
    user_controller.create_user(data['name'], data['username'], data['password'], data['user_level'], data['image'], data['status'])
    return jsonify({'message': 'User added successfully!'})

@app.route('/users/<int:user_id>', methods=['PUT'])
@authenticate
def update_user(user_id):
    data = request.json
    user_controller.update_user(user_id, data['name'], data['username'], data['password'], data['user_level'], data['image'], data['status'])
    return jsonify({'message': 'User updated successfully!'})

@app.route('/users/<int:user_id>', methods=['DELETE'])
@authenticate
def delete_user(user_id):
    user_controller.remove_user(user_id)
    return jsonify({'message': 'User deleted successfully!'})

@app.route('/user_groups', methods=['GET'])
@authenticate
def list_user_groups():
    user_groups = user_group_controller.get_all_user_groups()
    return jsonify(user_groups)

@app.route('/user_groups', methods=['POST'])
@authenticate
def add_user_group():
    data = request.json
    user_group_controller.create_user_group(data['name'])
    return jsonify({'message': 'User group added successfully!'})

@app.route('/user_groups/<int:user_group_id>', methods=['PUT'])
@authenticate
def update_user_group(user_group_id):
    data = request.json
    user_group_controller.update_user_group(user_group_id, data['name'])
    return jsonify({'message': 'User group updated successfully!'})

@app.route('/user_groups/<int:user_group_id>', methods=['DELETE'])
@authenticate
def delete_user_group(user_group_id):
    user_group_controller.remove_user_group(user_group_id)
    return jsonify({'message': 'User group deleted successfully!'})

if __name__ == '__main__':
    app.run(debug=True)