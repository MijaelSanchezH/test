
import sqlite3

conn = sqlite3.connect("equipos.db")
c = conn.cursor()

c.execute('DROP TABLE IF EXISTS equipos')
c.execute('DROP TABLE IF EXISTS historial')

c.execute('''
    CREATE TABLE equipos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        sala TEXT,
        nombre TEXT,
        temperatura TEXT,
        estado TEXT
    )
''')

c.execute('''
    CREATE TABLE historial (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        fecha TEXT,
        evento TEXT,
        estado TEXT
)
''')

equipos = [
    ("Sala Servidores", "AAP-SS-01", "23 °C", "Operativo"),
    ("Sala Servidores", "AAP-SS-02", "22 °C", "Operativo"),
    ("Sala Servidores", "AAP-SS-03", "20 °C", "Stand-by"),
    ("Sala Servidores", "AAP-SS-04", "21 °C", "Stand-by"),
    ("Sala UPS", "AAP-UPS-01", "22 °C", "Operativo")
]

c.executemany("INSERT INTO equipos (sala, nombre, temperatura, estado) VALUES (?, ?, ?, ?)", equipos)

historial = [
    ("AAP-SS-01", "2025/07/16 16:15", "Fallo ventilador UC", "Atendido"),
    ("AAP-SS-01", "2025/07/16 16:30", "Apagado manual", "Atendido"),
    ("AAP-SS-01", "2025/07/16 17:00", "Encendido manual", "Atendido"),
    ("AAP-SS-02", "2025/07/24 04:21", "Baja Presión", "Atendido"),
    ("AAP-SS-02", "2025/07/24 06:25", "Baja Presión", "Atendido"),
    ("AAP-SS-02", "2025/07/23 09:14", "Baja Presión", "Atendido"),
    ("AAP-SS-02", "2025/07/22 01:30", "Baja Presión", "Atendido"),
    ("AAP-SS-02", "2025/07/22 03:17", "Baja Presión", "Atendido"),
    ("AAP-SS-02", "2025/07/21 12:11", "Baja Presión", "Atendido"),
    ("AAP-SS-02", "2025/07/20 16:01", "Baja Presión", "Atendido"),
    ("AAP-SS-02", "2025/07/20 18:24", "Baja Presión", "Atendido"),
    ("AAP-SS-02", "2025/07/20 19:11", "Baja Presión", "Atendido"),
    ("AAP-SS-02", "2025/07/16 20:29", "Baja Presión", "Atendido"),
    ("AAP-SS-02", "2025/07/15 03:47", "Baja Presión", "Atendido"),
    ("AAP-SS-02", "2025/07/14 05:47", "Baja Presión", "Atendido"),
    ("AAP-SS-02", "2025/07/14 08:29", "Baja Presión", "Atendido"),
    ("AAP-SS-02", "2025/07/13 06:24", "Baja Presión", "Atendido"),
    ("AAP-SS-02", "2025/07/13 14:58", "Baja Presión", "Atendido"),
    ("AAP-SS-02", "2025/07/13 18:26", "Baja Presión", "Atendido"),
    ("AAP-SS-02", "2025/07/12 02:57", "Baja Presión", "Atendido"),
    ("AAP-SS-02", "2025/07/11 20:47", "Baja Presión", "Atendido"),
    ("AAP-SS-02", "2025/07/11 22:34", "Baja Presión", "Atendido"),
    ("AAP-SS-02", "2025/07/10 01:14", "Baja Presión", "Atendido"),
    ("AAP-SS-02", "2025/07/10 03:22", "Baja Presión", "Atendido"),
    ("AAP-SS-02", "2025/07/10 06:42", "Baja Presión", "Atendido"),
    ("AAP-SS-02", "2025/07/10 12:21", "Baja Presión", "Atendido"),
    ("AAP-SS-02", "2025/07/19 00:14", "Baja Presión", "Atendido"),
    ("AAP-SS-02", "2025/07/19 05:16", "Baja Presión", "Atendido"),
    ("AAP-SS-02", "2025/07/19 09:25", "Baja Presión", "Atendido")
]

c.executemany("INSERT INTO historial (nombre, fecha, evento, estado) VALUES (?, ?, ?, ?)", historial)

conn.commit()
conn.close()
print("Base de datos creada.")
