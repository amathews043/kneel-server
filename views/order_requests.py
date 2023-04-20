import sqlite3
import json

from models import Order, Metal, Size, Style

def get_all_orders():
    """function to get the orders"""

    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT 
            o.id as order_id,
            o.metal_id as metal_id,
            o.size_id as size_id,
            o.style_id as style_id,
            o.timestamp as timestamp,
            m.metal as metal_name,
            m.price as metal_price, 
            s.carets as carets, 
            s.price as carets_price,
            st.style as style,
            st.price as style_price
        FROM Orders o
        JOIN Metals m 
            on m.id = o.metal_id
        JOIN Sizes s
            on s.id = o.size_id
        JOIN Styles as st
            on st.id = o.style_id
        """)

        orders = []

        dataset =db_cursor.fetchall()
    
    for row in dataset: 
        order = Order(row['order_id'], row['metal_id'], row['size_id'], row['style_id'], row['timestamp'])

        metal = Metal(row['metal_id'], row['metal_name'], row['metal_price'])
        order.metal = metal.__dict__

        size = Size(row['size_id'], row['carets'], row['carets_price'])
        order.size = size.__dict__

        style = Style(row['style_id'], row['style'], row['style_price'])
        order.style = style.__dict__

        orders.append(order.__dict__)

    return orders

def get_single_order(id):
    """function to get a single order from the database"""

    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn: 
        conn.row_factory = sqlite3.Row

        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT 
            o.id as order_id, 
            o.metal_id as metal_id,
            o.size_id as size_id,
            o.style_id as style_id,
            o.timestamp as timestamp,
            m.metal as metal_name,
            m.price as metal_price, 
            s.carets as carets, 
            s.price as carets_price,
            st.style as style,
            st.price as style_price
        FROM Orders o
        JOIN Metals m 
            on m.id = o.metal_id
        JOIN Sizes s
            on s.id = o.size_id
        JOIN Styles as st
            on st.id = o.style_id
        WHERE o.id = ?
        """, (id, ))

        data = db_cursor.fetchone()

        order = Order(data['order_id'], data['metal_id'], data['size_id'], data['style_id'], data['timestamp'])
        size = Size(data['size_id'], data['carets'], data['carets_price'])
        order.size = size.__dict__
        metal = Metal(data['metal_id'], data['metal_name'], data['metal_price'])
        order.metal = metal.__dict__
        style = Style(data['style_id'], data['style'], data['style_price'])
        order.style = style.__dict__

    return order.__dict__

def create_order(order):
    """function to create an order"""
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:

        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Orders
            (metal_id, size_id, style_id, timestamp)
        VALUES 
            (?, ?, ?, ?);
        """, (order['metal_id'], order['size_id'], order['style_id'], order['timestamp'], ))

        id = db_cursor.lastrowid
        order['id'] = id

    return order

def delete_order(id):
    """Function to delete an order from the database"""
    with sqlite3.connect ("./kneeldiamonds.sqlite3") as conn: 

        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM Orders 
        WHERE id = ?
        """, (id, ))

def update_order(id, new_order):
    """function to update an existing order"""

    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn: 
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Orders 
            SET 
                metal_id = ?, 
                size_id = ?, 
                style_id = ?, 
                timestamp = ?
        WHERE id = ?
        """, (new_order['metal_id'], new_order['size_id'], new_order['style_id'], new_order['timestamp'], id))

        rows_affected = db_cursor.rowcount

        if rows_affected == 0: 
            return False 
        else: 
            return True
