from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/usuarios', methods=['GET'])
def obtener_usuario():
    return jsonify([
        {"id": 1, "nombre": "Franco", "edad": 22},
        {"id": 2, "nombre": "Yael", "edad": 21}
    ])
    
    
    
if __name__ == "__main__":
    app.run(port=5001)
    