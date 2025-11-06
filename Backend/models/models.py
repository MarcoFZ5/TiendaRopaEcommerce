from main import db

class Producto(db.Model):
    __tablename__ = "T_Producto"
    __table_args__ = {"schema": "SC_TiendaRopa"}

    id_producto = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(50), nullable = False)
    descripcion = db.Column(db.String(150), nullable = False)
    precio = db.Column(db.Numeric, nullable = False )
    stock = db.Column(db.Integer, nullable = False)
    talla = db.Column(db.Numeric, nullable = False)
    id_categoria = db.Column(db.Integer, db.ForeignKey("SC_TiendaRopa.T_Categoria.id_categoria"), nullable = False)

    categoria = db.relationship("Categoria", backref = "productos")

class Categoria(db.Model):
    __tablename__ = "T_Categoria"
    __table_args__ = {"schema": "SC_TiendaRopa"}

    id_categoria = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(50), nullable = False)
    descripcion = db.Column(db.String(50), nullable = False)