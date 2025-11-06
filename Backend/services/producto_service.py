from models.models import Producto

def traerProductos():
    return Producto.query.all()