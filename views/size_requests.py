import sqlite3
import json

from models import Size

SIZES = [
        { 
            "id": 1, 
            "carets": 0.5, 
            "price": 405 
        },

        { 
            "id": 2, 
            "carets": 0.75, 
            "price": 782 
        },

        { 
            "id": 3, 
            "carets": 1, 
            "price": 1470 
        },

        { 
            "id": 4, 
            "carets": 1.5, 
            "price": 1997 
        },

        { 
            "id": 5, 
            "carets": 2, 
            "price": 3638 
        }
    ]

def get_all_sizes():
    """function to get all size options """

    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn: 
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT 
            s.id,
            s.carets,
            s.price
        FROM Sizes s
        """)

        sizes = []

        dataset = db_cursor.fetchall()

    for row in dataset: 
        size = Size(row['id'], row['carets'], row['price'])

        sizes.append(size.__dict__)

    return sizes

def get_single_size(id):
    """function to get a single size from the database"""

    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row

        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT 
            s.id,
            s.carets,
            s.price
        FROM Sizes s
        WHERE id = ?
        """, (id, ))

        data = db_cursor.fetchone()

        size = Size(data['id'], data['carets'], data['price'])

        return size.__dict__
