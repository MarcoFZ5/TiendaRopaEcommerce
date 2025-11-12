from models.models import Carrito, ProductoVariacion, ProductoCarrito, Producto
from main import db

def obtener_detalle_carrito(carrito):
    producto_detalle = []
    total = 0

    for producto in carrito:
        variacion: ProductoVariacion = ProductoVariacion.query.get(producto["id_variacion"])

        subtotal = int(producto["cantidad"]) * float(variacion.precio)
        total += subtotal

        if producto:
            producto_detalle.append({
                "id_variacion": variacion.id_variacion,
                "nombre": variacion.producto.nombre,
                "talla": variacion.talla,
                "cantidad": producto["cantidad"],
                "precio": variacion.precio,
                "subtotal": subtotal
            })

    return total, producto_detalle

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

def eliminar(carrito, id_variacion):
    return [producto for producto in carrito if int(producto["id_variacion"]) != int(id_variacion)]

    
