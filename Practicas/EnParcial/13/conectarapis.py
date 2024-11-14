import requests
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/datos_juntos', methods=['GET'])
def datosjuntos():
    # Realizar solicitudes a las otras APIs
    usuarios = requests.get('http://127.0.0.1:5001/usuarios').json()
    productos = requests.get('http://127.0.0.1:5002/productos').json()
    
    # Devolver los datos combinados
    return jsonify({"usuarios": usuarios, "productos": productos})

if __name__ == "__main__":
    app.run(port=5000)
