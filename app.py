from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def hola_mundo():
    return jsonify({"mensaje": "¡Hola! Mi práctica funciona"})

@app.route('/salud')
def salud():
    return jsonify({"estado": "ok"})

@app.route('/secreto')
def secreto():
    secreto_simulado = "***CONEXION_BD_OCULTA***"
    return jsonify({
        "secreto_enmascarado": secreto_simulado,
        
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
