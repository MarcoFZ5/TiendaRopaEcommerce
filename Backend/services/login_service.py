USUARIO_ADMIN = "ADMIN"
PASSWORD_ADMIN = "12345"

def verificarDatos(username: str, password: str):
     return "ADMIN" if username == USUARIO_ADMIN and password == PASSWORD_ADMIN else "USUARIO"
    
    
