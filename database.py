import sqlite3

def create_connection():
    conn = sqlite3.connect('store.db')
    return conn

def create_tables():
    conn = create_connection()
    cursor = conn.cursor()

    # Tabela de produtos
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')

    # Tabela de pedidos
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY,
            customer_name TEXT NOT NULL,
            product_id INTEGER NOT NULL,
            quantity INTEGER NOT NULL,
            FOREIGN KEY (product_id) REFERENCES products (id)
        )
    ''')

    conn.commit()
    conn.close()

def add_product(name, price):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO products (name, price) VALUES (?, ?)', (name, price))
    conn.commit()
    conn.close()

def get_products():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM products')
    products = cursor.fetchall()
    conn.close()
    return products

def delete_product(product_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM products WHERE id = ?', (product_id,))
    conn.commit()
    conn.close()

def add_order(customer_name, product_id, quantity):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO orders (customer_name, product_id, quantity) VALUES (?, ?, ?)', (customer_name, product_id, quantity))
    conn.commit()
    conn.close()

def get_orders():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT o.id, o.customer_name, p.name, o.quantity, p.price * o.quantity AS total
        FROM orders o
        JOIN products p ON o.product_id = p.id
    ''')
    orders = cursor.fetchall()
    conn.close()
    return orders

def delete_order(order_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM orders WHERE id = ?', (order_id,))
    conn.commit()
    conn.close()

create_tables()
