from flask import Blueprint, render_template, session

carrito_bp = Blueprint("carrito_bp", __name__)

@carrito_bp.route("/carrito")
def carrito():
    carrito = session.get("carrito", [])
    return render_template("carrito.html", carrito = carrito)