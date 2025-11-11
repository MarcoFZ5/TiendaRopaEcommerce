from sqlalchemy.orm import joinedload

from models.models import Producto

def traerProductos(page: int):
    return (
        Producto.query
        .options(joinedload(Producto.tallas))
        .order_by(Producto.id_producto)
        .paginate(page=page, per_page=20))
    
def traerProductosPorCategoria(categoria: str, page: int):
    return (
        Producto.query
        .filter_by(id_categoria=categoria)
        .options(joinedload(Producto.tallas))
        .order_by(Producto.id_producto)
        .paginate(page=page, per_page=10)
    )