import sqlite3
import json

from models import Metal

METALS = [
    {
        "id": 1,
        "metal": "Sterling Silver",
        "price": 12.42
    },
    {
        "id": 2,
        "metal": "14K Gold",
        "price": 736.4
    },
    {
        "id": 3,
        "metal": "24K Gold",
        "price": 1258.9
    },
    {
        "id": 4,
        "metal": "Platinum",
        "price": 795.45
    },
    {
        "id": 5,
        "metal": "Palladium",
        "price": 1241
    }
]

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