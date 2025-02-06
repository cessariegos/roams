from flask import Flask, jsonify, request
from transformers import pipeline
import sqlite3

app = Flask(__name__)
generator = pipeline("text-generation", model = "flax-community/gpt-2-spanish")

def createDB():
    conn = sqlite3.connect("solicitudes.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS historial (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   prompt TEXT NOT NULL,
                   response TEXT NOT NULL
                   )""")
    conn.commit()
    conn.close()

createDB()

def insertDB(prompt, response):
    conn = sqlite3.connect("solicitudes.db")
    cursor = conn.cursor() 
    cursor.execute("INSERT INTO historial (prompt, response) VALUES (?, ?)", (prompt, response)) 
    conn.commit()
    conn.close()

@app.route("/solicitudes", methods = ["GET"])
def mostrar_solicitudes():
    conn = sqlite3.connect("solicitudes.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM historial ORDER BY id DESC")
    solicitudes = cursor.fetchall()
    conn.close()

    lista_solicitudes = [
        {"id": i[0], "prompt": i[1], "response": i[2]} for i in solicitudes
    ]

    return jsonify({"Solicitudes": lista_solicitudes})

@app.route("/texto", methods = ["POST"])
def generar_texto():
    data = request.get_json()
    
    prompt = data.get("prompt", "")
    max_length = data.get("max_length", "")
    # Menor temperature -> Mas predecible
    # Mayor temperature -> Mas creatividad 
    temperature = data.get("temperature", "")
    # Menor top_p -> Respuestas mas repetitivas
    # Mayor top_p -> Respuestas mas variadas
    top_p = data.get("top_p", "")

    if not prompt:
        return jsonify({"Error": "Se requiere un prompt para generar el texto"}), 400
    
    if not isinstance(max_length, int) or not (0 < max_length <= 1000):
        return jsonify({"Error": "La longitud máxima del texto debe ser un número entero entre 0 y 1000"}), 400
    
    if not isinstance(temperature, (int, float)) or not (0.2 <= temperature <= 1.2):
        return jsonify({"Error": "La variable temperature debe ser un número entre 0.2 y 1.2"}), 400
    
    if not isinstance(top_p, float) or not (0.4 <= top_p <= 0.9):
        return jsonify({"Error": "La variable top_p debe ser un número entre 0.4 y 0.9"}), 400

    result = generator(
        prompt, 
        max_length = max_length, 
        temperature = temperature, 
        top_p = top_p, 
        num_return_sequences = 1)
    
    respuesta = result[0]["generated_text"]

    insertDB(prompt, respuesta)
    
    return jsonify({"Texto:": respuesta})

if __name__ == '__main__':
    app.run(debug=True)
