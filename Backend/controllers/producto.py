from flask import Blueprint, render_template
from services.producto_service import producto_unico

producto_bp = Blueprint("producto_bp", __name__)

@producto_bp.route("/producto/<int:id>")
def producto(id):
    producto = producto_unico(id)

    return render_template("producto.html", producto=producto)

