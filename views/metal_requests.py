import sqlite3
import json

from models import Metal


def get_all_metals():
    """function to get all metals"""

    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn: 
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT 
            m.id, 
            m.metal, 
            m.price 
        FROM Metals m
        """)

        metals = []

        dataset = db_cursor.fetchall()

        for row in dataset: 
            metal = Metal(row['id'], row['metal'], row['price'])

            metals.append(metal.__dict__)
            
        return metals

def get_single_metal(id):
    """function to get a single metal from the database"""

    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn: 
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT 
            m.id, 
            m.metal, 
            m.price 
        FROM Metals m
        WHERE id = ?
        """, (id, )) 

        data = db_cursor.fetchone()

        metal = Metal(data['id'], data['metal'], data['price'])

    return metal.__dict__

def update_metal(id, new_metal): 
    """function to update a metal record"""

    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn: 

        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Metals 
            SET 
                metal = ?, 
                price = ?
        WHERE id = ?
        """, (new_metal['metal'], new_metal['price'], id ),)

        rows_affected = db_cursor.rowcount

    if rows_affected == 0: 
        return False 
    else: 
        return True
