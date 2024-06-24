import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from database import add_product, get_products, delete_product, add_order, get_orders, delete_order

def add_product_window():
    def submit_product():
        name = name_entry.get()
        price = price_entry.get()
        if name and price:
            try:
                price = float(price)
                add_product(name, price)
                messagebox.showinfo("Success", "Product added successfully!")
                add_window.destroy()
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid price")
        else:
            messagebox.showerror("Error", "Please enter both name and price")

    add_window = tk.Toplevel(root)
    add_window.title("Add Product")
    add_window.geometry("300x200")
    
    frame = ttk.Frame(add_window, padding="10")
    frame.pack(fill=tk.BOTH, expand=True)
    
    ttk.Label(frame, text="Product Name").grid(row=0, column=0, pady=5, sticky=tk.W)
    name_entry = ttk.Entry(frame)
    name_entry.grid(row=0, column=1, pady=5)
    
    ttk.Label(frame, text="Product Price").grid(row=1, column=0, pady=5, sticky=tk.W)
    price_entry = ttk.Entry(frame)
    price_entry.grid(row=1, column=1, pady=5)
    
    ttk.Button(frame, text="Add Product", command=submit_product).grid(row=2, columnspan=2, pady=20)

def show_products_window():
    products = get_products()
    
    show_window = tk.Toplevel(root)
    show_window.title("Products List")
    show_window.geometry("400x300")
    
    frame = ttk.Frame(show_window, padding="10")
    frame.pack(fill=tk.BOTH, expand=True)
    
    for product in products:
        product_label = ttk.Label(frame, text=f"ID: {product[0]} | Name: {product[1]} | Price: ${product[2]:.2f}")
        product_label.pack(pady=2, anchor=tk.W)
        delete_button = ttk.Button(frame, text="Delete", command=lambda p_id=product[0]: delete_product_and_refresh(p_id, show_window))
        delete_button.pack(pady=2, anchor=tk.W)

def delete_product_and_refresh(product_id, window):
    delete_product(product_id)
    window.destroy()
    show_products_window()

def add_order_window():
    def submit_order():
        customer_name = customer_name_entry.get()
        product_id = product_id_entry.get()
        quantity = quantity_entry.get()
        if customer_name and product_id and quantity:
            try:
                product_id = int(product_id)
                quantity = int(quantity)
                add_order(customer_name, product_id, quantity)
                messagebox.showinfo("Success", "Order placed successfully!")
                order_window.destroy()
            except ValueError:
                messagebox.showerror("Error", "Please enter valid product ID and quantity")
        else:
            messagebox.showerror("Error", "Please enter all fields")

    order_window = tk.Toplevel(root)
    order_window.title("Place Order")
    order_window.geometry("300x250")
    
    frame = ttk.Frame(order_window, padding="10")
    frame.pack(fill=tk.BOTH, expand=True)
    
    ttk.Label(frame, text="Customer Name").grid(row=0, column=0, pady=5, sticky=tk.W)
    customer_name_entry = ttk.Entry(frame)
    customer_name_entry.grid(row=0, column=1, pady=5)
    
    ttk.Label(frame, text="Product ID").grid(row=1, column=0, pady=5, sticky=tk.W)
    product_id_entry = ttk.Entry(frame)
    product_id_entry.grid(row=1, column=1, pady=5)
    
    ttk.Label(frame, text="Quantity").grid(row=2, column=0, pady=5, sticky=tk.W)
    quantity_entry = ttk.Entry(frame)
    quantity_entry.grid(row=2, column=1, pady=5)
    
    ttk.Button(frame, text="Place Order", command=submit_order).grid(row=3, columnspan=2, pady=20)

def show_orders_window():
    orders = get_orders()
    
    show_window = tk.Toplevel(root)
    show_window.title("Orders List")
    show_window.geometry("500x400")
    
    frame = ttk.Frame(show_window, padding="10")
    frame.pack(fill=tk.BOTH, expand=True)
    
    for order in orders:
        order_label = ttk.Label(frame, text=f"Order ID: {order[0]} | Customer: {order[1]} | Product: {order[2]} | Quantity: {order[3]} | Total: ${order[4]:.2f}")
        order_label.pack(pady=2, anchor=tk.W)
        delete_button = ttk.Button(frame, text="Delete", command=lambda o_id=order[0]: delete_order_and_refresh(o_id, show_window))
        delete_button.pack(pady=2, anchor=tk.W)

def delete_order_and_refresh(order_id, window):
    delete_order(order_id)
    window.destroy()
    show_orders_window()

root = tk.Tk()
root.title("Order Management System")
root.geometry("400x300")

frame = ttk.Frame(root, padding="20")
frame.pack(fill=tk.BOTH, expand=True)

ttk.Button(frame, text="Add Product", command=add_product_window).pack(pady=10)
ttk.Button(frame, text="Show Products", command=show_products_window).pack(pady=10)
ttk.Button(frame, text="Place Order", command=add_order_window).pack(pady=10)
ttk.Button(frame, text="Show Orders", command=show_orders_window).pack(pady=10)

root.mainloop()
