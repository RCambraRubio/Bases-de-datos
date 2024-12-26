import sqlite3

conexion = sqlite3.connect("database/negocio") # Se conecta a la BBDD, si no existe la creará
cursor = conexion.cursor()

sentencias = """
CREATE INDEX idx_fecha_pedido ON pedidos (fecha_pedido);
CREATE INDEX idx_id_pedido ON pedidos (id_pedido);
CREATE INDEX idx_pedidos_id_usuario ON pedidos (id_usuario);
               
CREATE INDEX idx_detalle_id_pedido ON detalles_pedido (id_pedido);
               
CREATE INDEX idx_id_pago ON pagos (id_pago);
CREATE INDEX idx_fecha_pago ON pagos (fecha_pago);
               
CREATE INDEX idx_almacen_id_producto ON movimiento_almacen (id_producto);
CREATE INDEX idx_fecha_movimiento ON movimiento_almacen (fecha_movimiento);
"""

# Ejecutar las sentencias
cursor.executescript(sentencias)

# Confirmar los cambios y cerrar la conexión
conexion.commit()
conexion.close()
