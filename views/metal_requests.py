import sqlite3
import json

from models import Metal

def get_all_metals(query_params={}):
    """function to get all metals"""

    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn: 
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        sort_by = ""

        if '_sortBy' in query_params: 
            if query_params['_sortBy'][0] == 'price':
                sort_by = "ORDER BY m.price"
        db_cursor.execute(f"""
        SELECT 
            m.id, 
            m.metal, 
            m.price 
        FROM Metals m
        {sort_by}
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