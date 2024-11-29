import sqlite3

def conectar_bd():
    conexion = sqlite3.connect("tienda.db")
    cursor = conexion.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            piezas_por_caja INTEGER,
            precio_por_pieza REAL,
            precio_total REAL,
            precio_venta REAL,
            tipo_de_producto TEXT
        )
    ''')
    conexion.commit()
    conexion.close()