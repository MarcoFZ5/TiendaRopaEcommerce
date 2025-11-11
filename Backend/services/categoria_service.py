from models.models import Categoria

def traerCategorias():
    return Categoria.query.all()
