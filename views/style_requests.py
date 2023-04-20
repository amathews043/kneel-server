import sqlite3
import json

from models import Style

STYLES = [
        { 
            "id": 1, 
            "style": "Classic", 
            "price": 500 
        },
        { 
            "id": 2, 
            "style": "Modern", 
            "price": 710 
        },
        { 
            "id": 3, 
            "style": "Vintage", 
            "price": 965 
        }
    ]

def get_all_styles():
    """function to get all styles from database"""

    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn: 

        conn.row_factory = sqlite3.Row 
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT 
            s.id, 
            s.style, 
            s.price
        FROM Styles s 
        """)

        styles = []
        dataset = db_cursor.fetchall()

    for row in dataset: 
        style = Style(row['id'], row['style'], row['price'])

        styles.append(style.__dict__)

    return styles


def get_single_style(id):
    # Variable to hold the found animal, if it exists
    requested_style = None

    # Iterate the ANIMALS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for style in STYLE:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if style["id"] == id:
            requested_style = style

    return requested_style