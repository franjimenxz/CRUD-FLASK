from flask import Flask, request, jsonify, render_template, redirect, url_for
from models import db, Product

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


# API RESTful
@app.route('/api/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify([product.to_dict() for product in products])

@app.route('/api/products', methods=['POST'])
def create_product():
    data = request.json
    product = Product(name=data['name'], price=data['price'])
    db.session.add(product)
    db.session.commit()
    return jsonify(product.to_dict()), 201

@app.route('/api/products/<int:id>', methods=['PUT'])
def update_product(id):
    data = request.json
    product = Product.query.get(id)
    if product:
        product.name = data['name']
        product.price = data['price']
        db.session.commit()
        return jsonify(product.to_dict())
    return jsonify({'error': 'Product not found'}), 404

@app.route('/api/products/<int:id>', methods=['DELETE'])
def delete_product_api(id):
    product = Product.query.get(id)
    if product:
        db.session.delete(product)
        db.session.commit()
        return jsonify({'message': 'Product deleted'})
    return jsonify({'error': 'Product not found'}), 404

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
