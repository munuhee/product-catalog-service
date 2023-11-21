from flask import jsonify, request
from app import app, db
from app.models.product import Product

@app.route('/status')
def hello_world():
    return jsonify({"message" : "application is healthy"}), 200

@app.route('/product-create', methods = ['POST'])
def create_product():
    try:
        data = request.get_json()
        new_product = Product(
            name = data["name"],
            description = data["description"],
            category = data["category"],
            price = data["price"],
        )

        db.session.add(new_product)
        db.session.commit()
        return jsonify({"message":"product added successfully"}), 201
    except KeyError as e:
        return f"mising field: {e}", 400
    except Exception as e:
        db.session.rollback()
        return str(e), 500

@app.route('/products', methods=['GET'])
def get_products():
    try:
        products = Product.query.all()
        formated_products = [{
            "id": product.id,
            "name": product.name,
            "description": product.description,
            "category": product.category,
            "price": product.price,
            "date_added": product.date_added.strftime("%Y-%m-%d %H:%M:%S")
        } for product in products]

        if formated_products:
            return jsonify(formated_products), 200
        else:
            return jsonify({"message": "No products found"}), 404

    except Exception as e:
        return jsonify({"message": "Error occurred", "error": str(e)}), 500
