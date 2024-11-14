from flask import Flask, jsonify, request

app = Flask(__name__)

def cargar_datos(cantidad):
    datos = []
    with open("info.txt") as archivo:
        for i, contenido in enumerate(archivo):
            if i < cantidad:
                datos.append(contenido.strip())
    return datos

@app.route('/datos/<int:cantidad>', methods=['GET'])
def obtener_datos(cantidad):
    datos = cargar_datos(cantidad)
    return jsonify({"usuarios": datos})

if __name__ == "__main__":
    app.run(debug=True)