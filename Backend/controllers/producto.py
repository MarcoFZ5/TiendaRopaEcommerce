from flask import Blueprint, render_template, request, session, redirect
from services.producto_service import producto_unico

producto_bp = Blueprint("producto_bp", __name__)

@producto_bp.route("/producto/<int:id>")
def producto(id):
    producto = producto_unico(id)

    return render_template("producto.html", producto=producto)

@producto_bp.route("/agregar_carrito", methods = ["POST"])
def agregar_carrito():
    item = {
        "id_producto": request.form["id_producto"],
        "id_variacion": request.form["id_variacion"],
        "talla": request.form["talla"],
        "cantidad": int(request.form["cantidad"]),
        "precio": float(request.form["precio"])
    }

    carrito = session.get("carrito", [])

    carrito.append(item)
    session["carrito"] = carrito

    return redirect("/carrito")
