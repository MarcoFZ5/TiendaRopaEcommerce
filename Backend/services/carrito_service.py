from models.models import Carrito, ProductoVariacion, ProductoCarrito
from main import db

def crear_carrito():
    carrito_bd = Carrito(metodo_pago="TARJETA")
    db.session.add(carrito_bd)
    db.session.commit()

    return carrito_bd


def insertar_productos(carrito, carrito_bd: Carrito):
    total = 0

    for producto in carrito:
        variacion = ProductoVariacion.query.get(producto["id_variacion"])

        if not variacion:
            continue
        
        subtotal = float(producto["precio"]) * int(producto["cantidad"])
        total += subtotal

        producto_carrito = ProductoCarrito(
            id_carrito = carrito_bd.id_carrito,
            id_variacion = producto["id_variacion"],
            cantidad = producto["cantidad"],
            subtotal = subtotal
        )

        db.session.add(producto_carrito)

        variacion.stock -= producto["cantidad"]

    carrito_bd.total = total

    db.session.commit()