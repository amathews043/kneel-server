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