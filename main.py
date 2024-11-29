import tkinter as tk
from bd_manager import conectar_bd
from funciones import ventana_agregar, mostrar_productos, ventana_modificar, ventana_filtrar, calcular_ganancias, importar_csv, exportar_csv, generar_reporte, notificar_stock_bajo

def main():
    # Crear la base de datos y la tabla si no existe
    conectar_bd()

    ventana = tk.Tk()
    ventana.title("Gestión de Inventario")
    ventana.geometry("400x600")
    ventana.resizable(False, False)

    tk.Button(ventana, text="Agregar Producto", command=lambda: ventana_agregar(ventana), font=("Arial", 12)).pack(pady=10)
    
    tk.Button(ventana, text="Mostrar Productos (ID y Nombre)", command=lambda: mostrar_productos(ventana), font=("Arial", 12)).pack(pady=10)
    
    tk.Button(ventana, text="Modificar Producto", command=lambda: ventana_modificar(ventana), font=("Arial", 12)).pack(pady=10)
    
    tk.Button(ventana, text="Filtrar Productos", command=lambda: ventana_filtrar(ventana), font=("Arial", 12)).pack(pady=10)
    
    tk.Button(ventana, text="Calcular Ganancias", command=calcular_ganancias, font=("Arial", 12)).pack(pady=10)
    
    tk.Button(ventana, text="Importar CSV", command=importar_csv, font=("Arial", 12)).pack(pady=10)
    
    tk.Button(ventana, text="Exportar CSV", command=exportar_csv, font=("Arial", 12)).pack(pady=10)
    
    tk.Button(ventana, text="Generar Reporte", command=generar_reporte, font=("Arial", 12)).pack(pady=10)
    
    tk.Button(ventana, text="Notificar Stock Bajo", command=notificar_stock_bajo, font=("Arial", 12)).pack(pady=10)
    
    tk.Button(ventana, text="Salir", command=ventana.destroy, font=("Arial", 12), fg="red").pack(pady=10)

    ventana.mainloop()

if __name__ == "__main__":
    main()