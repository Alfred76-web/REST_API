import requests
import json

API_URL = 'http://127.0.0.1:5000/products'

# Function to add a new product
def add_product(name, description, price):
    product_data = {
        'name': name,
        'description': description,
        'price': price
    }
    response = requests.post(API_URL, json=product_data)
    if response.status_code == 201:
        print(f"Product created: {response.json()}")
    else:
        print(f"Error: {response.status_code}, {response.json()}")

# Function to get the list of all products
def get_products():
    response = requests.get(API_URL)
    if response.status_code == 200:
        print(f"Products: {json.dumps(response.json(), indent=2)}")
    else:
        print(f"Error: {response.status_code}, {response.json()}")

if __name__ == "__main__":
    # Add products
    add_product("Product A", "Description of Product A", 19.99)
    add_product("Product B", "Description of Product B", 29.99)
    
    # Retrieve and print all products
    get_products()
