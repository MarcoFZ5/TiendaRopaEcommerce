from flask import Blueprint, render_template, session, redirect
from services.carrito_service import crear_carrito, insertar_productos, obtener_detalle_carrito

carrito_bp = Blueprint("carrito_bp", __name__)

@carrito_bp.route("/carrito")
def carrito():
    carrito_session = session.get("carrito", [])

    total, carrito_detalle = obtener_detalle_carrito(carrito_session)

    return render_template("carrito.html", productos=carrito_detalle, total=total)

@carrito_bp.route("/procesar_carrito", methods=["POST"])
def procesar_carrito():
    carrito_session = session.get("carrito", [])

    if not carrito_session:
        return "No hay productos en el carrito", 400
    
    carrito_bd = crear_carrito()

    insertar_productos(carrito_session, carrito_bd=carrito_bd)

    session.pop("carrito", None)

    return redirect("/")
    