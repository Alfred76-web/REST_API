import requests

response = requests.get("http://127.0.0.1:5000/products")
if response.status_code == 200:
    products = response.json()
    print("Products:", products)
else:
    print(f"Failed to retrieve products: {response.status_code}")
