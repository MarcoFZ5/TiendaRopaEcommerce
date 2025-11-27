from sqlalchemy.orm import joinedload

from models.models import Producto, ProductoVariacion

def productos_todos():
    return Producto.query.options(joinedload(Producto.tallas))

def variaciones(id):
    return ProductoVariacion.query.filter_by(id_producto=id).all()
