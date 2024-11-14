from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/contar/<string:palabra>', methods=['GET'])
def contar_letras(palabra):
    cantidad_letras = len(palabra)
    return jsonify({"palabra": palabra, "cantidad": cantidad_letras})

if __name__ == "__main__":
    app.run(debug=True)