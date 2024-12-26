import sqlite3
from datetime import datetime

conexion = sqlite3.connect("database/negocio") # Se conecta a la BBDD, si no existe la creará
cursor = conexion.cursor()

#####################################################
#                   INSERT                          #
#####################################################
# Insertar varios valores en la tabla movimiento_almacen
# Gracias al trigger trigger_de_movimientos_a_almacen cuando se haga el insert en la tabla movimiento_almacen se actualizará o, si no existe, se añadirá un registro en la tabla productos
cursor.execute('''
INSERT INTO movimiento_almacen (id_movimiento, id_producto, fecha_movimiento, stock)
VALUES 
    (1, 2, ?, 5),
    (2, 3, ?, 8);
''',(datetime.now(), datetime.now()))

# Insertar categorias
cursor.execute('''
INSERT INTO categorias (id_categoria, descripcion, nombre)
VALUES 
    (1, 'noseque', 'categoria 1'),
    (2, 'noseque 2', 'categoria 2');
''')

# Insertar usuarios
cursor.execute('''
INSERT INTO usuarios (id_usuario, nombre, apellidos, correo)
VALUES 
    (1, 'Juan', 'Palomo', 'jpalomo@gmail.com'),
    (2, 'Armando', 'Borncas', 'elbroncas@gmail.com'),
    (3, 'Pere', 'Gil', 'gilpere@gmail.com');
''')

# Insertar pedidos
cursor.execute('''
INSERT INTO pedidos (direccion_entrega, estado, fecha_entrega, fecha_pedido, id_usuario)
VALUES 
    ('su casa', 'entregado', datetime('2024-12-20 00:00:00'), datetime('2024-12-18 00:00:00'), 1),
    ('su casa', 'entregado', datetime('2024-12-10 00:00:00'), datetime('2024-12-08 00:00:00'), 1),
    ('su casa', 'entregado', datetime('2024-12-20 00:00:00'), datetime('2024-12-18 00:00:00'), 2),
    ('su casa', 'pendiente', NULL, datetime('2024-12-18 00:00:00'), 1);
''')

# Insertar los detalles de pedido
cursor.execute('''
INSERT INTO detalles_pedido (cantidad, id_pedido, id_producto, precio)
VALUES 
    (1, 1, 1, 5.5),
    (1, 1, 2, 1.2),
    (2, 2, 1, 10.6),
    (1, 3, 1, 5.2),
    (2, 3, 2, 2.3),
    (3, 4, 1, 15.8);
''')


#####################################################
#                   UPDATE                          #
#####################################################
# Actualizar / Modificar un registro de la tabla usuarios
cursor.execute(''' 
UPDATE usuarios
SET apellidos = 'bronca',
    correo = 'elbronca@gmail.com'
WHERE
    id_usuario = 2;
''')

# Actualizar / Modificar las categorias de los productos
cursor.execute(''' 
UPDATE productos
SET id_categoria = 1
WHERE
    id_producto = 1;
''')
cursor.execute(''' 
UPDATE productos
SET id_categoria = 2
WHERE
    id_producto = 2;
''')


#####################################################
#                   DELETE                          #
#####################################################
# Eliminar un registro de la tabla usuarios
cursor.execute(''' 
DELETE FROM usuarios
WHERE id_usuario = 3
''')

# Confirmar los cambios y cerrar la conexión
conexion.commit()
conexion.close()