from sqlalchemy.orm import joinedload
from main import db

from models.models import Producto, ProductoVariacion

def productos_todos():
    return Producto.query.options(joinedload(Producto.tallas))

def insertar_producto(producto):
    nuevo_producto = Producto(
        nombre = producto["nombre"],
        descripcion = producto["descripcion"],
        id_categoria = producto["id_categoria"])
    
    db.session.add(nuevo_producto)
    db.session.commit()
    
def producto(id):
    return Producto.query.filter_by(id_producto=id).first_or_404()

def borrar_producto(id):
    producto_borrar = producto(id)

    if producto:
        db.session.delete(producto_borrar)
        db.session.commit()

def modificar_producto(id, item):
    producto_a_modificar = producto(id=id)

    producto_a_modificar.nombre = item["nombre"]
    producto_a_modificar.descripcion = item["descripcion"]
    producto_a_modificar.id_categoria = item["id_categoria"]

    db.session.commit()

def variaciones(id):
    return ProductoVariacion.query.filter_by(id_producto=id).all()

def insertar_variacion(variacion):
    nueva_variacion = ProductoVariacion(
        id_producto = variacion["id_producto"],
        talla = variacion["talla"],
        stock = variacion["stock"],
        precio = variacion["precio"]
    )

    db.session.add(nueva_variacion)
    db.session.commit()

def variacion(id):
    return ProductoVariacion.query.filter_by(id_variacion=id).first_or_404()

def borrar_variacion(id):
    variacion_borrar = variacion(id=id)

    if variacion:
        db.session.delete(variacion_borrar)
        db.session.commit()

def modificar_variacion(id, producto):
    variacion_a_modificar = variacion(id)

    variacion_a_modificar.id_producto = producto["id_producto"]
    variacion_a_modificar.talla = producto["talla"]
    variacion_a_modificar.stock = producto["stock"]
    variacion_a_modificar.precio = producto["precio"]

    db.session.commit()
