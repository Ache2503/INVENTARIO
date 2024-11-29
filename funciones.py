import os
import openpyxl
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import sqlite3
import csv
from ui_utils import configurar_ventana
from bd_manager import conectar_bd

# Función para mostrar productos en una ventana secundaria
def mostrar_productos(ventana_principal):
    ventana = tk.Toplevel(ventana_principal)
    configurar_ventana(ventana, "Mostrar Productos", ventana_principal)

    # Conexión a la base de datos
    conexion = sqlite3.connect("tienda.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT id,  nombre. FROM productos")  # Solo seleccionamos Nombre y tipo
    productos = cursor.fetchall()
    conexion.close()

    # Estilo para la tabla
    estilo = ttk.Style()
    estilo.configure("Treeview", rowheight=70, font=("Arial", 12))  # Altura de filas y tamaño de fuente
    estilo.configure("Treeview.Heading", font=("Arial", 14, "bold"))  # Tamaño y estilo de las cabeceras

    # Tabla Treeview
    tabla = ttk.Treeview(ventana, columns=("ID", "Nombre"), show="headings")
    tabla.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    # Configurar el ancho de las columnas
    tabla.column("ID", width=300, anchor=tk.CENTER)
    tabla.column("Nombre", width=300, anchor=tk.W)

    # Encabezados de la tabla
    tabla.heading("ID", text="ID")
    tabla.heading("Nombre", text="Nombre")

    # Insertar datos en la tabla
    for producto in productos:
        tabla.insert("", tk.END, values=producto)

    # Barra de desplazamiento
    scrollbar = ttk.Scrollbar(ventana, orient=tk.VERTICAL, command=tabla.yview)
    tabla.configure(yscroll=scrollbar.set)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Función para agregar un producto
def ventana_agregar(ventana_principal):
    def activar_teclado(event):
        os.system("input keyevent 3")  # Simula el botón de inicio para que el teclado reaparezca.

    def agregar_producto():
        nombre = entrada_nombre.get()
        piezas_por_caja = entrada_piezas.get()
        precio_por_pieza = entrada_precio_pieza.get()
        precio_venta = entrada_precio_venta.get()
        tipo_de_producto = entrada_tipo.get()

        if not (nombre and piezas_por_caja and precio_por_pieza and precio_venta and tipo_de_producto):
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return

        if not (piezas_por_caja.isdigit() and precio_por_pieza.replace('.', '', 1).isdigit() and precio_venta.replace('.', '', 1).isdigit()):
            messagebox.showerror("Error", "Por favor, introduce valores numéricos válidos.")
            return

        piezas_por_caja = int(piezas_por_caja)
        precio_por_pieza = float(precio_por_pieza)
        precio_venta = float(precio_venta)
        precio_total = piezas_por_caja * precio_por_pieza

        conexion = sqlite3.connect("tienda.db")
        cursor = conexion.cursor()
        cursor.execute('''
            INSERT INTO productos (nombre, piezas_por_caja, precio_por_pieza, precio_total, precio_venta, tipo_de_producto)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (nombre, piezas_por_caja, precio_por_pieza, precio_total, precio_venta, tipo_de_producto))
        conexion.commit()
        conexion.close()

        limpiar_campos()
        messagebox.showinfo("Éxito", "Producto agregado correctamente.")

    def limpiar_campos():
        entrada_nombre.delete(0, tk.END)
        entrada_piezas.delete(0, tk.END)
        entrada_precio_pieza.delete(0, tk.END)
        entrada_precio_venta.delete(0, tk.END)
        entrada_tipo.delete(0, tk.END)

    ventana_add = tk.Toplevel(ventana_principal)
    configurar_ventana(ventana_add, "Agregar Producto", ventana_principal)

    tk.Label(ventana_add, text="Nombre:").pack(pady=5)
    entrada_nombre = tk.Entry(ventana_add, font=("Arial", 12))
    entrada_nombre.pack(pady=5)

    tk.Label(ventana_add, text="Piezas por caja:").pack(pady=5)
    entrada_piezas = tk.Entry(ventana_add, font=("Arial", 12))
    entrada_piezas.pack(pady=5)

    tk.Label(ventana_add, text="Precio por pieza:").pack(pady=5)
    entrada_precio_pieza = tk.Entry(ventana_add, font=("Arial", 12))
    entrada_precio_pieza.pack(pady=5)

    tk.Label(ventana_add, text="Precio de venta:").pack(pady=5)
    entrada_precio_venta = tk.Entry(ventana_add, font=("Arial", 12))
    entrada_precio_venta.pack(pady=5)

    tk.Label(ventana_add, text="Tipo de producto:").pack(pady=5)
    entrada_tipo = tk.Entry(ventana_add, font=("Arial", 12))
    entrada_tipo.pack(pady=5)

    tk.Button(ventana_add, text="Agregar Producto", command=agregar_producto, font=("Arial", 12)).pack(pady=10)

def ventana_modificar(ventana_principal):
    def activar_teclado(event):
        os.system("input keyevent 3")  # Simula el botón de inicio para que el teclado reaparezca.

    def buscar_producto():
        id_producto = entrada_id.get()
        if not id_producto.isdigit():
            messagebox.showerror("Error", "Por favor, ingresa un ID válido.")
            return

        conexion = sqlite3.connect("tienda.db")
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM productos WHERE id = ?", (id_producto,))
        producto = cursor.fetchone()
        conexion.close()

        if producto:
            # Rellenar los campos con los datos del producto
            entrada_nombre.delete(0, tk.END)
            entrada_piezas.delete(0, tk.END)
            entrada_precio.delete(0, tk.END)
            entrada_venta.delete(0, tk.END)
            entrada_tipo.delete(0, tk.END)

            entrada_nombre.insert(0, producto[1])
            entrada_piezas.insert(0, producto[2])
            entrada_precio.insert(0, producto[3])
            entrada_venta.insert(0, producto[5])
            entrada_tipo.insert(0, producto[6])
        else:
            messagebox.showerror("Error", "Producto no encontrado.")

    def actualizar_producto():
        id_producto = entrada_id.get()
        if not id_producto:
            messagebox.showerror("Error", "Debes buscar y seleccionar un producto primero.")
            return

        nombre = entrada_nombre.get()
        piezas_por_caja = entrada_piezas.get()
        precio_por_pieza = entrada_precio.get()
        precio_venta = entrada_venta.get()
        tipo_de_producto = entrada_tipo.get()

        # Validar campos obligatorios (puedes omitir algunos si no son esenciales)
        if not (nombre and precio_venta):
            messagebox.showerror("Error", "Los campos 'Nombre' y 'Precio de Venta' son obligatorios.")
            return

        # Manejar valores opcionales y cálculos
        piezas_por_caja = int(piezas_por_caja) if piezas_por_caja.isdigit() else None
        precio_por_pieza = float(precio_por_pieza) if precio_por_pieza.replace('.', '', 1).isdigit() else None
        precio_venta = float(precio_venta)
        precio_total = piezas_por_caja * precio_por_pieza if piezas_por_caja and precio_por_pieza else None

        # Actualizar el producto en la base de datos
        conexion = sqlite3.connect("tienda.db")
        cursor = conexion.cursor()
        cursor.execute('''
            UPDATE productos
            SET nombre = ?, piezas_por_caja = ?, precio_por_pieza = ?, precio_total = ?, precio_venta = ?, tipo_de_producto = ?
            WHERE id = ?
        ''', (nombre, piezas_por_caja, precio_por_pieza, precio_total, precio_venta, tipo_de_producto, id_producto))
        conexion.commit()
        conexion.close()

        messagebox.showinfo("Éxito", "Producto actualizado correctamente.")
        ventana_modificar.destroy()

    ventana_modificar = tk.Toplevel(ventana_principal)
    configurar_ventana(ventana_modificar, "Modificar Producto", ventana_principal)

    # Campos para ingresar datos
    tk.Label(ventana_modificar, text="ID del Producto:").pack()
    entrada_id = tk.Entry(ventana_modificar, font=("Arial", 12))
    entrada_id.pack(pady=5)

    tk.Button(ventana_modificar, text="Buscar Producto", command=buscar_producto, font=("Arial", 12)).pack(pady=10)

    tk.Label(ventana_modificar, text="Nombre:").pack()
    entrada_nombre = tk.Entry(ventana_modificar, font=("Arial", 12))
    entrada_nombre.pack(pady=5)

    tk.Label(ventana_modificar, text="Piezas por Caja:").pack()
    entrada_piezas = tk.Entry(ventana_modificar, font=("Arial", 12))
    entrada_piezas.pack(pady=5)

    tk.Label(ventana_modificar, text="Precio por Pieza:").pack()
    entrada_precio = tk.Entry(ventana_modificar, font=("Arial", 12))
    entrada_precio.pack(pady=5)

    tk.Label(ventana_modificar, text="Precio de Venta:").pack()
    entrada_venta = tk.Entry(ventana_modificar, font=("Arial", 12))
    entrada_venta.pack(pady=5)

    tk.Label(ventana_modificar, text="Tipo de Producto:").pack()
    entrada_tipo = tk.Entry(ventana_modificar, font=("Arial", 12))
    entrada_tipo.pack(pady=5)

    tk.Button(ventana_modificar, text="Actualizar Producto", command=actualizar_producto, font=("Arial", 12)).pack(pady=10)
 
#Ventana para filtrar datos
def ventana_filtrar(ventana_principal):
    def filtrar_datos():
        criterio = filtro_combobox.get()
        valor = filtro_entry.get()

        if not criterio or not valor:
            messagebox.showerror("Error", "Por favor selecciona un criterio y escribe un valor.")
            return

        conexion = sqlite3.connect("tienda.db")
        cursor = conexion.cursor()

        try:
            query = f"SELECT * FROM productos WHERE {criterio} LIKE ?"
            cursor.execute(query, (f"%{valor}%",))
            resultados = cursor.fetchall()
        except sqlite3.OperationalError:
            messagebox.showerror("Error", "Criterio inválido.")
            conexion.close()
            return

        # Limpiar la tabla
        for item in tabla.get_children():
            tabla.delete(item)

        # Insertar los resultados filtrados
        for producto in resultados:
            tabla.insert("", tk.END, values=producto)

        conexion.close()

    ventana = tk.Toplevel(ventana_principal)
    configurar_ventana(ventana, "Filtrar Productos", ventana_principal)

    tk.Label(ventana, text="Selecciona un criterio:").pack(pady=5)
    filtro_combobox = ttk.Combobox(ventana, values=["id", "nombre", "tipo_de_producto"], state="readonly", font=("Arial", 12))
    filtro_combobox.pack(pady=5)

    tk.Label(ventana, text="Escribe el valor a buscar:").pack(pady=5)
    filtro_entry = tk.Entry(ventana, font=("Arial", 12))
    filtro_entry.pack(pady=5)

    tk.Button(ventana, text="Filtrar", command=filtrar_datos, font=("Arial", 12)).pack(pady=10)

    # Tabla Treeview para mostrar los datos filtrados
    estilo = ttk.Style()
    estilo.configure("Treeview", rowheight=70, font=("Arial", 12))
    estilo.configure("Treeview.Heading", font=("Arial", 14, "bold"))

    tabla = ttk.Treeview(ventana, columns=("ID", "Nombre", "Piezas por Caja", "Precio por Pieza", "Precio Total", "Precio Venta", "Tipo de Producto"), show="headings")
    tabla.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    # Configurar el ancho de las columnas
    tabla.column("ID", width=50, anchor=tk.CENTER)
    tabla.column("Nombre", width=200, anchor=tk.W)
    tabla.column("Piezas por Caja", width=150, anchor=tk.CENTER)
    tabla.column("Precio por Pieza", width=150, anchor=tk.CENTER)
    tabla.column("Precio Total", width=150, anchor=tk.CENTER)
    tabla.column("Precio Venta", width=150, anchor=tk.CENTER)
    tabla.column("Tipo de Producto", width=200, anchor=tk.W)

    # Encabezados de la tabla
    tabla.heading("ID", text="ID")
    tabla.heading("Nombre", text="Nombre")
    tabla.heading("Piezas por Caja", text="Piezas por Caja")
    tabla.heading("Precio por Pieza", text="Precio por Pieza")
    tabla.heading("Precio Total", text="Precio Total")
    tabla.heading("Precio Venta", text="Precio Venta")
    tabla.heading("Tipo de Producto", text="Tipo de Producto")

    # Barra de desplazamiento
    scrollbar = ttk.Scrollbar(ventana, orient=tk.VERTICAL, command=tabla.yview)
    tabla.configure(yscroll=scrollbar.set)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
# Función para calcular ganancias
def calcular_ganancias():
    conexion = sqlite3.connect("tienda.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT SUM((precio_venta - precio_por_pieza) * piezas_por_caja) AS ganancias FROM productos")
    resultado = cursor.fetchone()
    conexion.close()
    ganancias = resultado[0] if resultado[0] else 0
    messagebox.showinfo("Ganancias", f"Las ganancias potenciales son: ${ganancias:.2f}")

# Función para importar datos desde un archivo CSV
def importar_csv():
    archivo = filedialog.askopenfilename(filetypes=[("Archivos CSV", "*.csv")])
    if archivo:
        conexion = sqlite3.connect("tienda.db")
        cursor = conexion.cursor()
        with open(archivo, "r") as f:
            lector_csv = csv.reader(f)
            next(lector_csv)  # Omitir encabezados
            for fila in lector_csv:
                cursor.execute('''
                    INSERT INTO productos (nombre, piezas_por_caja, precio_por_pieza, precio_total, precio_venta, tipo_de_producto)
                    VALUES (?, ?, ?, ?, ?, ?)
                ''', fila)
        conexion.commit()
        conexion.close()
        messagebox.showinfo("Éxito", "Datos importados correctamente.")

# Función para exportar datos a un archivo CSV
def exportar_csv():
    archivo = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("Archivos CSV", "*.csv")])
    if archivo:
        conexion = sqlite3.connect("tienda.db")
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM productos")
        filas = cursor.fetchall()
        conexion.close()
        with open(archivo, "w", newline="") as f:
            escritor_csv = csv.writer(f)
            escritor_csv.writerow(["ID", "Nombre", "Piezas por Caja", "Precio por Pieza", "Precio Total", "Precio de Venta", "Tipo de Producto"])
            escritor_csv.writerows(filas)
        messagebox.showinfo("Éxito", "Datos exportados correctamente.")

def generar_reporte():
    conexion = sqlite3.connect("tienda.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM productos")
    datos = cursor.fetchall()

    if not datos:
        messagebox.showinfo("Reporte", "No hay datos para generar el reporte.")
        conexion.close()
        return

    # Crear un nuevo archivo Excel
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = "Productos"

    # Encabezados
    encabezados = ["ID", "Nombre", "Piezas por Caja", "Precio por Pieza", "Precio Total", "Precio Venta", "Tipo de Producto"]
    sheet.append(encabezados)

    # Agregar datos
    for fila in datos:
        sheet.append(fila)

    # Guardar el archivo
    archivo = "Reporte_Productos.xlsx"
    workbook.save(archivo)
    conexion.close()
    messagebox.showinfo("Reporte", f"Reporte generado: {archivo}")

#Notificar stock bajo
def notificar_stock_bajo():
    conexion = sqlite3.connect("tienda.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT id, nombre, piezas_por_caja FROM productos WHERE piezas_por_caja < 5")
    productos_bajos = cursor.fetchall()

    if productos_bajos:
        mensaje = "Productos con stock bajo:\n"
        for producto in productos_bajos:
            mensaje += f"ID: {producto[0]}, Nombre: {producto[1]}, Piezas: {producto[2]}\n"
        messagebox.showwarning("Stock Bajo", mensaje)
    else:
        messagebox.showinfo("Stock", "No hay productos con stock bajo.")

    conexion.close()