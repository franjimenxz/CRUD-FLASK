from flask import Flask, request, jsonify
from math_operations import sumar, restar, multiplicar, dividir

app = Flask(__name__)

@app.route('/sumar', methods=['GET'])
def sumar_route():
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))
    result = sumar(a, b)
    return jsonify({'result': result})

@app.route('/restar', methods=['GET'])
def restar_route():
    num1 = float(request.args.get('a'))
    num2 = float(request.args.get('b'))
    result = restar(num1, num2)
    return jsonify({'result': result})

@app.route('/multiplicar', methods=['GET'])
def multiplicar_route():
    num1 = float(request.args.get('a'))
    num2 = float(request.args.get('b'))
    result = multiplicar(num1, num2)
    return jsonify({'result': result})

@app.route('/dividir', methods=['GET'])
def dividir_route():
    num1 = float(request.args.get('a'))
    num2 = float(request.args.get('b'))
    result = dividir(num1, num2)
    return jsonify({'result': result})

# Ruta de prueba
@app.route('/test', methods=['GET'])
def test_route():
    return "La ruta de prueba está funcionando"

if __name__ == '__main__':
    app.run(debug=True)
