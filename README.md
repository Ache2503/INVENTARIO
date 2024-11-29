Sistema de Gestión de Tienda

Descripción General:
Este proyecto es un sistema de gestión de tienda desarrollado con Python y Tkinter para facilitar tareas administrativas como la gestión de productos, usuarios, y generación de reportes. Incluye autenticación de usuarios con roles diferenciados: Administrador y Usuario.

El sistema utiliza SQLite como base de datos para el almacenamiento de productos, usuarios y un historial de modificaciones. También cuenta con funciones para exportar/importar datos y generar reportes en PDF y Excel.

Funcionalidades del Sistema
1. Inicio de Sesión:
Autenticación de usuarios con roles diferenciados.
Mantiene la sesión activa hasta que el usuario cierre sesión.

2. Rol Administrador:
Agregar, modificar y eliminar productos.
Ver y filtrar productos.
Exportar e importar datos del inventario.
Generar reportes en PDF y Excel.
Historial de modificaciones.

3. Rol Usuario:
Consultar productos disponibles.
Filtrar productos por diferentes criterios.



4. Diseño Modular:
Separación de funciones en archivos específicos:
Archivo principal: Maneja la lógica de inicio de sesión y navegación.
Funciones del administrador: Contiene las operaciones avanzadas.
Funciones del usuario: Operaciones básicas de consulta.
Base de datos: Estructura y manejo de datos.


Problemas Actuales o Áreas de Mejora

Estoy buscando colaboración para resolver los siguientes puntos o mejorar el sistema:

1. Interfaz Gráfica:
Asegurar que las ventanas se centren y se redimensionen correctamente en diferentes resoluciones.
Mejorar el diseño visual para hacerlo más profesional.

2. Historial de Modificaciones:
Añadir más detalles al historial, como el usuario que realizó el cambio.

3. Exportación e Importación:
Garantizar la compatibilidad con formatos CSV, Excel y PDF.
Agregar soporte para importar desde archivos con estructuras complejas.

4. Validación y Seguridad:
Mejorar la validación de datos en formularios.
Implementar un hash para contraseñas en lugar de almacenarlas en texto plano.

5. Pruebas y Documentación:
Crear casos de prueba para asegurar la funcionalidad del sistema.
Añadir documentación detallada para nuevos colaboradores.

Cómo Colaborar

Si deseas colaborar, aquí tienes algunos pasos para empezar:

1. Contribuye con tu Código o Mejoras:
Trabaja en las áreas mencionadas o en cualquier funcionalidad adicional.

2. Realiza un Pull Request:
Sube tus cambios y describe en detalle las mejoras.
Preguntas o Comentarios

Si tienes alguna duda o sugerencia, no dudes en abrir un issue o comunicarte a través de los comentarios del repositorio. ¡Toda colaboración es bienvenida!
