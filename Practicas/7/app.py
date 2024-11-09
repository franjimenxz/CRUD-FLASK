from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/multiplicar', methods=['GET'])
def multiplicar():
    num1=request.args.get('num1', '')
    num2=request.args.get('num2', '')
    result=num1*num2
    return jsonify('{result}, result')    

@app.route('/sumar', methods=['GET'])
def sumar():
    num1=request.args.get('num1', '')
    num2=request.args.get('num2', '')
    result=num1+num2
    return jsonify({'result': result})


if __name__ == '__main__':
    app.run(debug=True)
