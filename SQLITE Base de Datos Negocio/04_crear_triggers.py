import sqlite3

conexion = sqlite3.connect("database/negocio") # Se conecta a la BBDD, si no existe la creará
cursor = conexion.cursor()

# Cada vez que se inserte un registro en movimiento_almacen, se modificará el registro de ese producto en productos
# Si el producto no existe en la tabla producto se insertará un registro en esta tabla
cursor.execute('''
CREATE TRIGGER trigger_de_movimientos_a_almacen
AFTER INSERT ON movimiento_almacen
BEGIN
    -- Actualizar el stock de productos
    UPDATE productos
    SET stock = NEW.stock
    WHERE id_producto = NEW.id_producto;
    
    -- Insertar si no existe el registro en productos
    INSERT OR IGNORE INTO productos (id_producto, stock) 
    VALUES (NEW.id_producto, NEW.stock);
END;
''')


# Confirmar los cambios y cerrar la conexión
conexion.commit()
conexion.close()