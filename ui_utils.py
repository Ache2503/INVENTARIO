def configurar_ventana(ventana_secundaria, titulo, ventana_principal):
    ventana_secundaria.title(titulo)
    ventana_secundaria.geometry(ventana_principal.geometry())
    ventana_secundaria.resizable(False, False)