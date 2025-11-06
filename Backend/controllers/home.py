from flask import Blueprint, render_template
from services.producto_service import traerProductos

home_bp = Blueprint("home", __name__)

@home_bp.route("/")
def home():
    all_productos = traerProductos()
    return render_template("home.html", nombre = "Grupo 1", productos = all_productos)