from flask import Blueprint, render_template, request, redirect, session
from services.productos_service import productos_todos, variaciones, insertar_producto, borrar_producto, modificar_producto, insertar_variacion, borrar_variacion, variacion, modificar_variacion
from services.producto_service import producto_unico
from services.categoria_service import traerCategorias

productos_bp = Blueprint("productos", __name__)

@productos_bp.route("/productos")
def productos():
    all_productos = productos_todos()

    return render_template("productos.html", productos = all_productos)

@productos_bp.route("/agregarproducto", methods = ["GET", "POST"])
def agregar_producto():
    all_categorias = traerCategorias()

    if request.method == "POST":
        item = {
            "nombre": request.form["nombre"],
            "descripcion": request.form["descripcion"],
            "id_categoria": request.form["id_categoria"],
        }

        insertar_producto(item)
        return redirect("/productos")

    else:
        return render_template("agregar_producto.html", categorias = all_categorias)

@productos_bp.route("/eliminarproducto/<int:id>")
def eliminar_producto(id):
    borrar_producto(id=id)

    return redirect("/productos")

@productos_bp.route("/editarproducto/<int:id>", methods = ["GET", "POST"])
def editar_producto(id):
    all_categorias = traerCategorias()
    producto_solo = producto_unico(id=id)

    if request.method == "POST":
        producto = {
            "nombre": request.form["nombre"],
            "descripcion": request.form["descripcion"],
            "id_categoria": request.form["id_categoria"]
        }

        modificar_producto(id=id, item=producto)
        return redirect("/productos")

    else:
        return render_template("editar_producto.html", producto = producto_solo, categorias = all_categorias)
    
@productos_bp.route("/productovariacion/<int:id>")
def producto_variacion(id):
    producto = producto_unico(id)
    variaciones_producto = variaciones(id)

    return render_template("productoVariaciones.html", producto = producto, variaciones = variaciones_producto)

@productos_bp.route("/agregarvariacion/<int:id>", methods = ["GET", "POST"])
def agregar_variacion(id):
    producto_base = producto_unico(id)

    if request.method == "POST":
         print(request.form)
         variacion = {
            "id_producto": request.form["id_producto"],
            "talla": request.form["talla"],
            "stock": request.form["stock"],
            "precio": request.form["precio"]
         }
         insertar_variacion(variacion)
         return redirect("/productovariacion/"+str(id))
    
    else: 
        return render_template("agregar_variacion.html", producto = producto_base)

@productos_bp.route("/editarvariacion/<int:id>", methods = ["GET", "POST"])
def editar_variacion(id):
    variacion_unica = variacion(id=id)

    if request.method == "POST":
        variacion_modificada = {
            "id_producto": request.form["id_producto"],
            "talla" : request.form["talla"],
            "stock" : request.form["stock"],
            "precio" : request.form["precio"]
        }
        modificar_variacion(id=id, producto=variacion_modificada)
        return redirect("/productos")
    
    else:
        return render_template("editar_variacion.html", variacion = variacion_unica)


@productos_bp.route("/eliminarvariacion/<int:id>")
def eliminar_variacion(id):
    borrar_variacion(id=id)
    return redirect("/productos")