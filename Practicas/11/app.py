from flask import Flask, render_template

app = Flask(__name__)

@app.route('/imagen')
def mostrar_imagen():
    url_imagen = "https://diariohoynet.nyc3.cdn.digitaloceanspaces.com/adjuntos/galerias/000/565/0000565217.jpg"
    return render_template("mostrar_imagen.html", url_imagen=url_imagen)

if __name__ == "__main__":
    app.run(debug=True)
