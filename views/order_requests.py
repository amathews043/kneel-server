import sqlite3
import json

from models import Order, Metal, Size, Style


ORDERS = [
        {
            "id": 1,
            "metal_id": 3,
            "size_id": 2,
            "style_id": 3,
            "timestamp": 1614659931693
        }
    ]

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
    # Get the id value of the last order in the list
    max_id = ORDERS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the animal dictionary
    order["id"] = new_id

    # Add the animal dictionary to the list
    ORDERS.append(order)

    # Return the dictionary with `id` property added
    return order

def delete_order(id):
    # Initial -1 value for order index, in case one isn't found
    order_index = -1

    # Iterate the orderS list, but use enumerate() so that you
    # can access the index value of each item
    for index, order in enumerate(ORDERS):
        if order["id"] == id:
            # Found the order. Store the current index.
            order_index = index

    # If the order was found, use pop(int) to remove it from list
    if order_index >= 0:
        ORDERS.pop(order_index)

def update_order(id, new_order):
    # Iterate the orderS list, but use enumerate() so that
    # you can access the index value of each item.
    for index, order in enumerate(ORDERS):
        if order["id"] == id:
            # Found the order. Update the value.
            ORDERS[index] = new_order
            break
