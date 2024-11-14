from flask import Flask, request, jsonify

app = Flask(__name__)

#lista
nombres = []

@app.route('/nombres', methods=['GET'])
def traer():
    return jsonify({"nombres": nombres})


@app.route('/nombres', methods=['POST'])
def agregar():
    data = request.get_json()
    nombre = {
        "nombre" : data.get("nombre"),
    }
    nombres.append(nombre)
    return jsonify({"nombre": nombres}), 201

if __name__ == "__main__":
    app.run(debug=True)  