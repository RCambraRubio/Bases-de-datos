def visualizar(cursor, consulta):
    cursor.execute(consulta) # Consulta a la tabla
    registros = cursor.fetchall() # Recuperar todos los registros
    for registro in registros: # Mostrar los resultados
        print(registro)
