from flask import Blueprint, render_template, request, session, redirect
from services.login_service import verificarDatos

login_bp = Blueprint("login", __name__)

@login_bp.route("/login", methods = ["GET", "POST"])
def login():
    if request.method == "POST":
        usuario = request.form.get("username")
        password = request.form.get("password")

        rol_usuario = verificarDatos(usuario, password)

        if rol_usuario:
            session["rol"] = rol_usuario
            print(session.get("rol"))
            return redirect("/")
    else:
        return render_template("login.html")

@login_bp.route("/logout")
def logout():
    del session["rol"]
    return redirect("/")

    
