from flask import Blueprint, render_template, session, redirect
from services.carrito_service import crear_carrito, insertar_productos, obtener_detalle_carrito, eliminar, info_ventas

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

    return redirect("/carrito?success=1")
    
@carrito_bp.route("/eliminar_del_carrito/<int:id_variacion>", methods=["POST"])
def eliminar_del_carrito(id_variacion):
    carrito = session.get("carrito", [])

    carrito_modificado = eliminar(carrito, id_variacion)

    session["carrito"] = carrito_modificado
    session.modified = True

    return redirect("/carrito")

@carrito_bp.route("/info")
def informacion_ventas():
    ventas = info_ventas()

    labels = [v.fecha_creacion for v in ventas]
    datos = [v.total for v in ventas]

    return render_template("grafico.html", etiquetas = labels, data = datos)

@carrito_bp.route("/infobarras")
def informacion_ventas_barras():
    ventas = info_ventas()

    labels = [v.fecha_creacion for v in ventas]
    datos = [v.total for v in ventas]

    return render_template("graficobarras.html", etiquetas = labels, data = datos)