from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import time
import random

app = Flask(__name__)
# Habilitamos CORS para permitir peticiones desde el HTML local
CORS(app) 

# In-memory storage de puntos (simple, no persistente)
POINTS = []

@app.route('/guardar_punto', methods=['POST'])
def guardar_punto():
    data = request.json
    
    if not data:
        return jsonify({"error": "No data provided"}), 400

    lat = data.get('lat')
    lng = data.get('lng')
    
    print(f"📍 Recibiendo coordenadas: {lat}, {lng}")

    # --- SIMULACIÓN DE LATENCIA Y PROCESAMIENTO ---

    time.sleep(random.uniform(1.5, 3.0))

    # Simulamos un fallo aleatorio del 10% para probar el manejo de errores
    if random.random() < 0.1:
        return jsonify({"status": "error", "message": "Fallo simulado en base de datos"}), 500

    # Crear registro del punto y almacenarlo en memoria
    point_id = random.randint(1000, 9999)
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    point = {
        "id": point_id,
        "lat": lat,
        "lng": lng,
        "timestamp": timestamp,
        "address": f"Punto de Ruta #{len(POINTS) + 1}"
    }
    POINTS.append(point)

    response = {
        "status": "success",
        "message": "Punto guardado correctamente",
        "point": point
    }

    return jsonify(response), 200


@app.route('/puntos', methods=['GET'])
def get_puntos():
    # Devuelve la lista completa de puntos almacenados (no paginado)
    return jsonify({"points": POINTS}), 200

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/map')
def mapa():
    return render_template('mapa_integrado.html')

if __name__ == '__main__':
    print("🚀 Servidor ForLiveRunning activo en http://localhost:5000")
    app.run(debug=True, port=5000)
