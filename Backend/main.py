from flask import Flask, render_template
from config import Config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

@app.route("/")
def hello_world():
    return render_template("hello.html", nombre = "Grupo 1")

if __name__ == "__main__":
    with app.app_context():
        try:
            with db.engine.connect() as conn:
                print("Conectado correctamente a la base de datos")
        except Exception as e:
            print(f"Error al conectar: {e}")
    app.run(debug=True)
    pass