from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///usuarios.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# Definición del modelo de Usuario
class Usuario(db.Model):
    __tablename__ = "usuarios"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    edad = db.Column(db.Integer, nullable=False)
    correo = db.Column(db.String(100), nullable=False)


with app.app_context():
    db.create_all()
    
    # Agregar usuarios iniciales si la tabla está vacía
    if Usuario.query.count() == 0:
        usuarios_iniciales = [
            Usuario(nombre="Juan", edad=28, correo="juan@example.com"),
            Usuario(nombre="Maria", edad=25, correo="maria@example.com"),
            Usuario(nombre="Luis", edad=30, correo="luis@example.com"),
            Usuario(nombre="Ana", edad=22, correo="ana@example.com"),
            Usuario(nombre="Carlos", edad=35, correo="carlos@example.com")
        ]
        db.session.add_all(usuarios_iniciales)
        db.session.commit()
        
                
#Endpoint de obtencion y agregar

# Endpoint para mostrar una cantidad específica de usuarios
@app.route('/usuarios/<int:cantidad>', methods=['GET'])
def obtener_usuarios(cantidad):
    # Consulta los usuarios y limita la cantidad solicitada
    usuarios = Usuario.query.limit(cantidad).all()    
    # Convertir los objetos de usuario en diccionarios para el JSON de respuesta
    usuarios_lista = [{"id": u.id, "nombre": u.nombre, "edad": u.edad, "correo": u.correo} for u in usuarios]
    
    return jsonify(usuarios_lista)


# Endpoint para agregar un nuevo usuario
@app.route('/usuarios', methods=['POST'])
def agregar_usuario():
    datos = request.get_json()  # Obtener los datos enviados en formato JSON
    nombre = datos.get("nombre")
    edad = datos.get("edad")
    correo = datos.get("correo")
    
    # Crear el nuevo usuario
    nuevo_usuario = Usuario(nombre=nombre, edad=edad, correo=correo)
    
    # Agregar y confirmar los cambios en la base de datos
    db.session.add(nuevo_usuario)
    db.session.commit()
    
    return jsonify({"mensaje": "Usuario agregado correctamente", "usuario": {
        "id": nuevo_usuario.id, "nombre": nuevo_usuario.nombre, "edad": nuevo_usuario.edad, "correo": nuevo_usuario.correo
    }}), 201  # 201 indica que se creó un recurso


if __name__ == "__main__":
    app.run(debug=True)
