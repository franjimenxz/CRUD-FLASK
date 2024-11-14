from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/productos', methods=['GET'])
def obtenerproducto():
    return jsonify([
       {"id": 1, "nombre": "Notebook", "precio": 2222},
        {"id": 2, "nombre": "Celular", "precio": 2121}
    ])
    
if __name__ == "__main__":
    app.run(port=5002)
    
    