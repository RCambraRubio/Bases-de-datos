import sqlite3
from datetime import datetime

conexion = sqlite3.connect("database/negocio") # Se conecta a la BBDD, si no existe la creará
cursor = conexion.cursor()

# Añadir una columna a la tabla de usuarios
cursor.execute(''' 
ALTER TABLE usuarios
ADD COLUMN edad;
''')

# Eliminar la columna añadida de la tabla usuarios
# Para ello se crea una tabla temporal sin la columna y se cambia por la original
sentencias = """ 
CREATE TABLE IF NOT EXISTS usuarios_temp (
    id_usuario INTEGER PRIMARY KEY,
    nombre CHAR(50),
    apellidos CHAR(50),
    correo CHAR(100)
);

INSERT INTO usuarios_temp(id_usuario, nombre, apellidos, correo)
SELECT id_usuario, nombre, apellidos, correo
FROM usuarios;

ALTER TABLE usuarios RENAME TO usuarios_respaldo;

ALTER TABLE usuarios_temp RENAME TO usuarios;

DROP TABLE usuarios_respaldo;
"""
cursor.executescript(sentencias)


# Confirmar los cambios y cerrar la conexión
conexion.commit()
conexion.close()