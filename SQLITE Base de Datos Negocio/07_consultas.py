import sqlite3
import visualizar_datos_consulta

conexion = sqlite3.connect("database/negocio") # Se conecta a la BBDD, si no existe la creará
cursor = conexion.cursor()


print("1. Cuantos pructos están en movimiento_almacen y no están en productos")
print("Debería dar 0, si no es que hay algún producto que falta en la tabla productos")
consulta = """
    SELECT COUNT(DISTINCT movimiento_almacen.id_producto) AS "count"
    FROM movimiento_almacen
        LEFT JOIN productos 
            ON movimiento_almacen.id_producto = productos.id_producto
    WHERE productos.id_producto IS NULL
"""
visualizar_datos_consulta.visualizar(cursor, consulta)


print("2. Informacion de pedidos")
consulta = """
    SELECT 
        pedidos.id_pedido,
        usuarios.nombre,
        usuarios.apellidos,
        usuarios.correo,
        pedidos.estado,
        pedidos.fecha_pedido,
        SUM(detalles_pedido.precio) AS precio_total,
        GROUP_CONCAT('producto: ' || detalles_pedido.id_producto || ' cantidad: ' || detalles_pedido.cantidad, ', ') AS detalle

    FROM pedidos
        LEFT JOIN detalles_pedido
            ON pedidos.id_pedido = detalles_pedido.id_pedido
        LEFT JOIN usuarios
            ON usuarios.id_usuario = pedidos.id_usuario
    
    WHERE 
        pedidos.fecha_pedido -- Solo del mes de diciembre de 2024
            BETWEEN datetime('2024-12-01 00:00:00')
                AND datetime('2024-12-31 23:59:59')

    GROUP BY 
        pedidos.id_pedido,
        usuarios.nombre,
        usuarios.apellidos,
        usuarios.correo,
        pedidos.estado,
        pedidos.fecha_pedido

    ORDER BY pedidos.fecha_pedido DESC
""" 
visualizar_datos_consulta.visualizar(cursor, consulta)

print("3. Informacion de los productos con un pedido pendiente")
consulta ="""
    SELECT
        pedidos.id_pedido,
        pedidos.fecha_entrega,
        detalles_pedido.id_producto,
        detalles_pedido.cantidad,
        productos.stock,
        categorias.nombre AS categoria
    
    FROM pedidos
        LEFT JOIN detalles_pedido
            ON detalles_pedido.id_pedido = pedidos.id_pedido
        LEFT JOIN productos
            ON productos.id_producto = detalles_pedido.id_producto
        LEFT JOIN categorias
            ON categorias.id_categoria = productos.id_categoria
        
    WHERE pedidos.estado = 'pendiente'

    ORDER BY pedidos.fecha_pedido DESC
"""
visualizar_datos_consulta.visualizar(cursor, consulta)


# Confirmar los cambios y cerrar la conexión
conexion.commit()
conexion.close()
