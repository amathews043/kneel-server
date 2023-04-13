from .metal_requests import get_single_metal
from .size_requests import get_single_size
from .style_requests import get_single_style

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
    return ORDERS

def get_single_order(id):
    # Variable to hold the found animal, if it exists
    requested_order = None

    # Iterate the ANIMALS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for order in ORDERS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if order["id"] == id:
            requested_order = order.copy()
            metal = get_single_metal(requested_order["metal_id"])
            requested_order["metal"] = metal
            size = get_single_size(requested_order["size_id"])
            requested_order["size"] = size
            style = get_single_style(requested_order["style_id"])
            requested_order["style"] = style

    return requested_order

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
