import sqlite3
import os

# Muestra la ruta exacta para verificar que estés usando la correcta
print("📍 Usando base de datos:", os.path.abspath("equipos.db"))

# Datos a modificar
nombre_equipo = "AAP-SS-01"
nueva_temp = "150 °C"

# Conexión a la base de datos
conn = sqlite3.connect("equipos.db")
cur = conn.cursor()

# Actualizar temperatura
cur.execute("UPDATE equipos SET temperatura = ? WHERE nombre = ?", (nueva_temp, nombre_equipo))
conn.commit()

# Verificar actualización
cur.execute("SELECT * FROM equipos WHERE nombre = ?", (nombre_equipo,))
print("✅ Resultado actualizado:", cur.fetchone())

conn.close()
