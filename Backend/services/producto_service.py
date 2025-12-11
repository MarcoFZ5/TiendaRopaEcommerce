from sqlalchemy.orm import joinedload

from models.models import Producto

def traerProductos(page: int):
    return (
        Producto.query
        .options(joinedload(Producto.tallas))
        .order_by(Producto.id_producto)
        .paginate(page=page, per_page=8))
    
def traerProductosPorCategoria(categoria: str, page: int):
    return (
        Producto.query
        .filter_by(id_categoria=categoria)
        .options(joinedload(Producto.tallas))
        .order_by(Producto.id_producto)
        .paginate(page=page, per_page=8)
    )

def producto_unico(id: int):
    return (
        Producto.query
        .options(joinedload(Producto.tallas))
        .filter_by(id_producto=id)
        .first_or_404()
    )