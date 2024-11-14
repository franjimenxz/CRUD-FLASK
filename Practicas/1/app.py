#Api que reciba un objeto y se agregue a una lista.(post)
from flask import Flask, request, jsonify

app = Flask(__name__)

items = []

@app.route('/add_item', methods=['POST'])
def agregaritem():
    item = request.get_json()
    items.append(item)
    return jsonify({'items': items}), 201

if __name__ == '__main__':
    app.run()