from main import db
import datetime

class Producto(db.Model):
    __tablename__ = "T_Producto"
    __table_args__ = {"schema": "SC_TiendaRopa"}

    id_producto = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(50), nullable = False)
    descripcion = db.Column(db.String(150), nullable = False)
    id_categoria = db.Column(db.Integer, db.ForeignKey("SC_TiendaRopa.T_Categoria.id_categoria"), nullable = False)

    categoria = db.relationship("Categoria", backref = "productos")

    tallas = db.relationship("ProductoVariacion", backref="producto", lazy=True)

class Categoria(db.Model):
    __tablename__ = "T_Categoria"
    __table_args__ = {"schema": "SC_TiendaRopa"}

    id_categoria = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(50), nullable = False)
    descripcion = db.Column(db.String(50), nullable = False)

class ProductoVariacion(db.Model):
    __tablename__ = "T_ProductoVariacion"
    __table_args__ = {"schema": "SC_TiendaRopa"}

    id_variacion = db.Column(db.Integer, primary_key = True)
    id_producto = db.Column(db.Integer, db.ForeignKey("SC_TiendaRopa.T_Producto.id_producto"), nullable = False)
    talla = db.Column(db.String(150), nullable = False)
    stock = db.Column(db.Integer, nullable = False)
    precio = db.Column(db.Numeric, nullable = False)

class Carrito(db.Model):
    __tablename__ = "T_Carrito"
    __table_args__ = {"schema": "SC_TiendaRopa"}

    id_carrito = db.Column(db.Integer, primary_key=True)
    fecha_creacion = db.Column(db.DateTime, default=datetime.datetime.now())
    total = db.Column(db.Numeric, default=0)
    estado = db.Column(db.String(30), default="CREADO")
    metodo_pago = db.Column(db.String(50), nullable=False)

    productos = db.relationship("ProductoCarrito", backref="carrito", lazy=True)

class ProductoCarrito(db.Model):
    __tablename__ = "T_ProductoCarrito"
    __table_args__ = {"schema": "SC_TiendaRopa"}

    id_producto_carrito = db.Column(db.Integer, primary_key=True)
    id_carrito = db.Column(db.Integer, db.ForeignKey("SC_TiendaRopa.T_Carrito.id_carrito"))
    id_variacion = db.Column(db.Integer, db.ForeignKey("SC_TiendaRopa.T_ProductoVariacion.id_variacion"))
    cantidad = db.Column(db.Integer, nullable=False)
    subtotal = db.Column(db.Numeric, nullable=False)
