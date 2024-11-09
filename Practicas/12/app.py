from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def mostrar_archivo():
        # Leer el contenido del archivo local
    with open("prueba.txt") as archivo:
        contenido_archivo = archivo.read()
        
        # Pasar el contenido al template para renderizarlo
    return render_template("mostrar_archivo.html", contenido=contenido_archivo)
    
if __name__ == "__main__":
    app.run(debug=True)
