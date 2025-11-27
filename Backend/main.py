from flask import Flask
from config import Config
from database import db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    from controllers.login import login_bp
    from controllers.home import home_bp
    from controllers.producto import producto_bp
    from controllers.productos import productos_bp
    from controllers.carrito import carrito_bp

    app.register_blueprint(login_bp)
    app.register_blueprint(home_bp)
    app.register_blueprint(producto_bp)
    app.register_blueprint(productos_bp)
    app.register_blueprint(carrito_bp)

    return app

if __name__ == "__main__":
    app = create_app()

    with app.app_context():
        try:
            with db.engine.connect() as conn:
                print("Conectado correctamente a la base de datos")
        except Exception as e:
            print(f"Error al conectar: {e}")

    app.run(debug=True)