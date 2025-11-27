from flask import Blueprint, render_template, request, redirect, session
from services.productos_service import productos_todos, variaciones
from services.producto_service import producto_unico

productos_bp = Blueprint("productos", __name__)

@productos_bp.route("/productos")
def productos():
    all_productos = productos_todos()

    return render_template("productos.html", productos = all_productos)

@productos_bp.route("/productovariacion/<int:id>")
def producto_variacion(id):
    producto = producto_unico(id)
    variaciones_producto = variaciones(id)

    return render_template("productoVariaciones.html", producto = producto, variaciones = variaciones_producto)
