from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/division', methods=['GET'])
def division():
    num1 = request.args.get('num1', type=float)
    num2 = request.args.get('num2', type=float)
    resultado = num1 / num2
    
    return jsonify({"resultado": resultado})

if __name__ == "__main__":
    app.run(debug=True)
    
    #http://127.0.0.1:5000/division?num1=100&num2=10
    
    