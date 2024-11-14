from flask import Flask, render_template

app = Flask(__name__)

@app.route('/mostrar_imagen')
def mostrar_imagen():
    url_imagen = "https://resizer.iproimg.com/unsafe/1280x/filters:format(webp)/https://assets.iprofesional.com/assets/jpg/2020/09/502789.jpg"
    return render_template("index.html", url_imagen=url_imagen)

if __name__ == "__main__":
    app.run(debug=True)