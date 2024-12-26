from eralchemy.main import render_er

# Ruta de entrada (base de datos SQLite) y salida (archivo de imagen)
input_path = "sqlite:///database/negocio"
output_path = "diagrama.png"

# Generar el archivo gráfico
render_er(input_path, output_path)
print(f"Diagrama generado en {output_path}")
