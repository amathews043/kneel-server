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

def get_all_styles(query_params={}):
    """function to get all styles from database"""

    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn: 

        conn.row_factory = sqlite3.Row 
        db_cursor = conn.cursor()

        sort_by = ""

        if '_sortBy' in query_params: 
            if query_params["_sortBy"][0] == "price":
                sort_by = "ORDER BY s.price"

        db_cursor.execute(f"""
        SELECT 
            s.id, 
            s.style, 
            s.price
        FROM Styles s 
        {sort_by}
        """)

        styles = []
        dataset = db_cursor.fetchall()

    for row in dataset: 
        style = Style(row['id'], row['style'], row['price'])

        styles.append(style.__dict__)

    return styles


def get_single_style(id):
    """function to get a single style from the database"""

    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn: 
        conn.row_factory = sqlite3.Row

        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT 
            s.id, 
            s.style, 
            s.price
        FROM Styles s 
        WHERE id = ?
        """, (id, ))

        data = db_cursor.fetchone()

        style = Style(data['id'], data['style'], data['price'])

        return style.__dict__
    
def update_style(id, style):
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn: 
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Styles 
        SET 
            style = ?, 
            price = ?
        WHERE id = ?
        """, (style['style'], style['price'], id ))