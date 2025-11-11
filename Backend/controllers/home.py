from flask import Blueprint, render_template, request
from services.producto_service import traerProductos, traerProductosPorCategoria
from services.categoria_service import traerCategorias

home_bp = Blueprint("home", __name__)

@home_bp.route("/")
def home():
    # Opciones
    pagina = request.args.get("page", 1, type=int)
    categoria = request.args.get("categoria", type= int)

    all_categorias = traerCategorias()

    if categoria:
        all_productos = traerProductosPorCategoria(categoria, page=pagina)
    else:
        all_productos = traerProductos(page=pagina)

    return render_template("home.html", nombre = "Grupo 1", productos = all_productos, categorias = all_categorias, categoria_actual = categoria)