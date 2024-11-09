from flask import Flask, request, jsonify

app = Flask(__name__)

#lista
names = []

@app.route('/names', methods=['GET'])
def traer():
    return jsonify({"names": names})


@app.route('/names', methods=['POST'])
def agregar():
    new_name = request.get_json()
    names.append(new_name)
    return jsonify({"name": new_name}), 201

if __name__ == "__main__":
    app.run(debug=True)