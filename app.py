
from flask import Flask, jsonify, request
import sqlite3
from flask_cors import CORS
from collections import Counter
from datetime import datetime

app = Flask(__name__,static_folder="static",template_folder="templates")
CORS(app)

def get_db_connection():
    conn = sqlite3.connect("equipos.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/api/equipos")
def api_equipos():
    conn = get_db_connection()
    equipos = conn.execute("SELECT sala, nombre, temperatura, estado FROM equipos").fetchall()
    conn.close()

    return jsonify([dict(e) for e in equipos])

@app.route("/api/equipo/<nombre>")
def equipo(nombre):
    conn = sqlite3.connect("equipos.db")
    c = conn.cursor()
    c.execute("SELECT fecha, evento, estado FROM historial WHERE nombre = ?", (nombre,))
    datos = c.fetchall()
    conn.close()

    historial = [{"fecha": f, "evento": e, "estado": s} for f, e, s in datos]
    return jsonify({"historial": historial})

@app.route("/api/histograma/<nombre>")
def histograma(nombre):
    conn = sqlite3.connect("equipos.db")
    c = conn.cursor()
    c.execute("SELECT fecha FROM historial WHERE nombre = ?", (nombre,))
    fechas_raw = c.fetchall()
    conn.close()

    dias = []
    for (f,) in fechas_raw:
        try:
            fecha = datetime.strptime(f, "%Y/%m/%d %H:%M")  # ← Este formato es correcto
            dias.append(fecha.day)
        except Exception as e:
            print(f"❌ Error convirtiendo fecha: {f} → {e}")

    conteo = Counter(dias)
    resultado = [{"dia": dia, "cantidad": conteo.get(dia, 0)} for dia in range(1, 32)]

    return jsonify(resultado)

@app.route("/")
def home():
    return render_tamplate("index.html")

if __name__ == "__main__":
    app.run(debug=True)
