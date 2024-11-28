from flask import Flask, request, jsonify

app = Flask(__name__)

# Route for the product API
@app.route('/products', methods=['GET'])
def get_products():
    # logic to retrieve products
    products = [{"name": "BMW M5", "description": "v6 Biturbo", "price": 8000000},
                {"name": "Audi R8", "description": "v10", "price": 12000000},
                {"name": "Mercedes Benz SLS", "description": "v8", "price": 15000000}
                ]
    return jsonify(products)

@app.route('/products', methods=['POST'])
def add_product():
    data = request.get_json()
    if not data or 'name' not in data or 'description' not in data or 'price' not in data:
        return jsonify({'error': 'Invalid input'}), 400
    new_product = {"name": data['name'], "description": data['description'], "price": data['price']}
    return jsonify(new_product), 201

if __name__ == '__main__':
    app.run(debug=True)
