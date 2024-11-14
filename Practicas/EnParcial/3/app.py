from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/sumar', methods=['POST'])
def suma():
    data = request.get_json()
    num1 = int(data.get('num1'))
    num2 = int(data.get('num2'))
    return jsonify(suma = num1+num2)

if __name__ == "__main__":
    app.run(debug=True)