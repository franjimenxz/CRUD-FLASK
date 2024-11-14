from flask import Flask, jsonify

app = Flask(__name__)

def cargardatos():
    datos = []
    with open("datos.txt") as archivo:
        for linea in archivo:
            usuario = {"datos": linea.strip()}
            datos.append(usuario)
    return datos 
        
@app.route('/datos', methods=['GET'])
def obtenerdatos():
    datos = cargardatos()
    return jsonify({"usuarios": datos})

if __name__ == "__main__":
    app.run(debug=True)
        