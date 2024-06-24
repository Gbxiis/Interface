# app/routes.py
from flask import render_template, request, redirect, url_for
from app import app
from database import get_products, add_product, get_orders, add_order

@app.route('/')
def home():
    products = get_products()
    orders = get_orders()
    return render_template('index.html', products=products, orders=orders)

@app.route('/add_product', methods=['GET', 'POST'])
def add_product_route():
    if request.method == 'POST':
        name = request.form['name']
        price = float(request.form['price'])
        add_product(name, price)
        return redirect(url_for('home'))
    return render_template('add_product.html')

@app.route('/add_order', methods=['GET', 'POST'])
def add_order_route():
    if request.method == 'POST':
        customer_name = request.form['customer_name']
        product_id = int(request.form['product_id'])
        quantity = int(request.form['quantity'])
        add_order(customer_name, product_id, quantity)
        return redirect(url_for('home'))
    products = get_products()
    return render_template('add_order.html', products=products)
