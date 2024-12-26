import sqlite3

conexion = sqlite3.connect("database/negocio") # Se conecta a la BBDD, si no existe la creará
cursor = conexion.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
    id_usuario INTEGER PRIMARY KEY,
    nombre CHAR(50),
    apellidos CHAR(50),
    correo CHAR(100)
)
''')


cursor.execute('''
CREATE TABLE IF NOT EXISTS categorias (
    id_categoria INTEGER PRIMARY KEY,
    nombre CHAR(50),
    descripcion TEXT
)
''')


cursor.execute('''
CREATE TABLE IF NOT EXISTS productos (
    id_producto INTEGER PRIMARY KEY,
    nombre CHAR(50),
    descripcion TEXT,
    stock INTEGER NOT NULL,
    id_categoria INTEGER,
    FOREIGN KEY (id_categoria) REFERENCES categorias (id_categoria)
)
''')


cursor.execute('''
CREATE TABLE IF NOT EXISTS movimiento_almacen (
    id_movimiento INTEGER PRIMARY KEY,
    id_producto INTEGER NOT NULL,
    fecha_movimiento DATETIME NOT NULL,
    stock INTEGER NOT NULL,
    FOREIGN KEY (id_producto) REFERENCES productos (id_producto)
)
''')


cursor.execute('''
CREATE TABLE IF NOT EXISTS pedidos (
    id_pedido INTEGER PRIMARY KEY AUTOINCREMENT,
    id_usuario INTEGER NOT NULL,
    fecha_pedido DATETIME,
    direccion_entrega TEXT NOT NULL,
    fecha_entrega DATETIME,
    estado TEXT NOT NULL,
    FOREIGN KEY (id_usuario) REFERENCES usuarios (id_usuario)
)
''')


cursor.execute('''
CREATE TABLE IF NOT EXISTS detalles_pedido (
    id_detalle INTEGER PRIMARY KEY AUTOINCREMENT,
    id_pedido INTEGER NOT NULL,
    id_producto INTEGER NOT NULL,
    cantidad INTEGER NOT NULL,
    precio FLOAT NOT NULL,
    FOREIGN KEY (id_pedido) REFERENCES pedidos (id_pedido),
    FOREIGN KEY (id_producto) REFERENCES productos (id_producto)
)
''')


cursor.execute('''
CREATE TABLE IF NOT EXISTS pagos (
    id_pago INTEGER PRIMARY KEY AUTOINCREMENT,
    id_pedido INTEGER NOT NULL,
    metodo CHAR(50),
    precio FLOAT NOT NULL,
    fecha_pago DATETIME,
    FOREIGN KEY (id_pedido) REFERENCES pedidos (id_pedido)
)
''')



# Confirmar los cambios y cerrar la conexión
conexion.commit()
conexion.close()