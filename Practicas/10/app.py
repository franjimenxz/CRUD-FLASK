from flask import Flask, request, jsonify

app = Flask(__name__)

#lista
users = []

@app.route('/users', methods=['GET'])
def traer():
    return jsonify({"user": users})


@app.route('/users', methods=['POST'])
def agregar():
    data = request.get_json()
    user = {
        "nombre" : data.get("nombre"),
        "edad" : data.get("edad"),
        "correo" : data.get("correo")
    }
    users.append(user)
    return jsonify({"name": users}), 201

if __name__ == "__main__":
    app.run(debug=True)