from flask import Flask, render_template, jsonify

app = Flask(__name__)


#api

@app.route('/api/mostrar_archivo', methods=['GET'])
def mostrar_api():
   with open("prueba.txt") as archivo:
        contenido_archivo = archivo.read()
        return jsonify({'contenido': contenido_archivo})



@app.route("/mostrar")
def mostrar_archivo():       
    response = app.test_client().get("/api/mostrar_archivo")
    data = response.get_json()

    # Pasar el contenido o error al template
    contenido = data.get("contenido")
    return render_template("mostrar_archivo.html", contenido = contenido)
    
if __name__ == "__main__":
    app.run(debug=True)
