import requests

# Data for a car-related product (e.g., car engine)
product_data = {
    "name": "V8 Engine",
    "description": "High-performance V8 engine for sports cars.",
    "price": 8999.99
}

# Sending POST request to the /products endpoint
response = requests.post("http://127.0.0.1:5000/products", json=product_data)

# Check if the product was added successfully
if response.status_code == 201:
    print("Product added successfully:", response.json())
else:
    print(f"Failed to add product: {response.status_code}")
