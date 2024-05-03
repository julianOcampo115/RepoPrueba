from flask import Blueprint, request, jsonify
from users.models.product_model import Products
from users.models.db import db

product_controller = Blueprint('product_controller', __name__)

@product_controller.route('/api/products', methods=['GET'])
def get_products():
    print("listado de productos")
    products = Products.query.all()
    result = [{'code':product.code, 'product': product.product, 'price': product.price, 'amount': product.amount, 'bag': product.bag} for product in products]
    return jsonify(result)

# Get single user by id
@product_controller.route('/api/products/<int:product_code>', methods=['GET'])
def get_product(product_code):
    print("obteniendo producto")
    product = Products.query.get_or_404(product_code)
    return jsonify({'code':product.code, 'product': product.product, 'price': product.price, 'amount': product.amount, 'bag': product.bag})

@product_controller.route('/api/products', methods=['POST'])
def create_product():
    print("creando producto")
    data = request.json
    new_product = Products(product=data['product'], price=data['price'], amount=data['amount'], bag=data['bag'])
    db.session.add(new_product)
    db.session.commit()
    return jsonify({'message': 'Product created successfully'}), 201

# Update an existing user
@product_controller.route('/api/products/<int:product_code>', methods=['PUT'])
def update_product(product_code):
    print("actualizando producto")
    product = Products.query.get_or_404(product_code)
    data = request.json
    product.product = data['product']
    product.price = data['price']
    product.amount = data['amount']
    product.bag = data['bag']
    db.session.commit()
    return jsonify({'message': 'Product updated successfully'})

# Delete an existing user
@product_controller.route('/api/products/<int:product_code>', methods=['DELETE'])
def delete_product(product_code):
    product = Products.query.get_or_404(product_code)
    db.session.delete(product)
    db.session.commit()
    return jsonify({'message': 'Product deleted successfully'})
