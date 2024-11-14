from flask import Flask, jsonify, request
from biblioteca import concatenar

app = Flask(__name__)

@app.route('/concatena', methods=['POST'])
def concatena():
    datos = request.get_json()
    palabra1= datos.get("palabra1", "")
    palabra2= datos.get("palabra2", "")
    
    resultado = concatenar(palabra1, palabra2)
    
    return jsonify({"resultado": resultado})

if __name__ == "__main__":
    app.run(debug=True)