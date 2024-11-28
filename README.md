# REST_API_FOR_MANAGING PRODUCTS

# SETTING UP THE ENVIRONMENT

## 1. Clone my repository
**git clone**  https://github.com/Alfred76-web/REST_API.git
**cd** github.com/Alfred76-web/REST_API.git


## 2. Set up and activate the Virtual Environment
python -m venv venv

.\venv\Scripts\activate

## 3. Install Dependencies
pip install -r requirements.txt
pip install flask

## 4. Verify the Installation
python -m flask --version

# Running the API Server
python app.py

The Url I used to access the server was: _http://127.0.0.1:5000/_

# Testing the API
## 1. Get All products
_http://127.0.0.1:5000/products_

For my case the output was:
[
  {
    "description": "v6 Biturbo",
    "name": "BMW M5",
    "price": 8000000
  },
  {
    "description": "v10",
    "name": "Audi R8",
    "price": 12000000
  },
  {
    "description": "v8",
    "name": "Mercedes Benz SLS",
    "price": 15000000
  }
]

## 2. Add new product
curl -X POST http://127.0.0.1:5000/products -H "Content-Type: application/json" -d '{"name": "V8 Engine", "description": "High-performance V8 engine for sports cars.", "price": 8999.99}'

# Using Python Requests

## 1. Get all products
Create a Python script _get_products.py_

## 2. A new product 
Create a Python script _add_car_product.py_:

## 3. Run python Scripts
python get_products.py  

python add_car_product.py   
<img width="471" alt="output" src="https://github.com/user-attachments/assets/7db03960-c0ec-4079-acbf-0c4fbf35b1ea">



