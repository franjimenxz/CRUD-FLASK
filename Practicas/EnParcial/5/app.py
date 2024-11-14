from flask import Flask, jsonify, request,render_template

app = Flask(__name__)

usuarios = []

@app.route('/agregar_usuario', methods=['POST'])
def agregar_usuarios():
    datos = request.get_json()
    nuevo_usuario = {
        "nombre" : datos["nombre"],
        "apellido": datos["apellido"]
    }
    usuarios.append(nuevo_usuario)
    return jsonify({"usuario": nuevo_usuario}), 201

@app.route('/usuarios', methods=['GET'])
def obtener_usuarios():
    return render_template("usuarios.html", usuarios=usuarios)

if __name__ == "__main__":
    app.run(debug=True)