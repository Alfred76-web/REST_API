# app.py
from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for products (this would normally be a database)
products = []

@app.route('/products', methods=['POST'])
def create_product():
    try:
        # Get JSON data from the request
        data = request.get_json()
        
        # Validate the input data
        if 'name' not in data or 'description' not in data or 'price' not in data:
            return jsonify({"error": "Invalid input, all fields (name, description, price) are required"}), 400
        
        # Create the product
        product = {
            "name": data["name"],
            "description": data["description"],
            "price": float(data["price"])
        }

        # Add the product to the in-memory storage
        products.append(product)

        # Return the product with status 201 Created
        return jsonify(product), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/products', methods=['GET'])
def get_products():
    # Return the list of products as JSON
    return jsonify(products), 200

if __name__ == '__main__':
    app.run(debug=True)
