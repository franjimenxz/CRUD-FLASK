#Api concatenar dos palabras.

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/concatenar', methods=['POST'])
def concatenar():
    words = request.get_json()
    word1= words.get('word1', '')
    word2= words.get('word2', '')
    return jsonify({'word': word1 + word2}),201
if __name__ == '__main__':
    app.run()