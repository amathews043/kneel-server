import sqlite3
import json

from models import Size

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
    
def update_size(id, new_size):
    """function to update a size record in the database"""
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn: 
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Sizes
            SET 
                carets = ?, 
                price = ?
        WHERE id = ?
        """, (new_size['carets'], new_size['price'], id))

        rows_affected = db_cursor.rowcount

    if rows_affected == 0: 
        return False 
    else: 
        return True
