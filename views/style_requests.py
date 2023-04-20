import sqlite3
import json

from models import Style

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
    
def update_style(id, new_style):
    """function to update an existing style record in the database"""

    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn: 
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Styles 
            SET
            style = ?, 
            price = ?
        WHERE id = ? 
        """, (new_style['style'], new_style['price'], id))

        rows_affected = db_cursor.rowcount

        if rows_affected == 0: 
            return False 
        else: 
            return True