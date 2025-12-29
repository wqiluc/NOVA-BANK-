from flask import (Flask, render_template, request, redirect, url_for)
from backending.novabank_frontending import (ver_saldo, depositar, sacar)

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/tela_inicio")
def tela_inicio():
    return render_template("tela_inicio.html")

@app.route("/tela_versaldo")
def tela_versaldo():
    return render_template("tela_versaldo.html", saldo=ver_saldo())

@app.route("/tela_depositarsaldo", methods=["GET", "POST"])
def tela_depositarsaldo():
    if request.method == "POST":
        depositar(int(request.form["valor"]))
        return redirect(url_for("tela_versaldo"))
    return render_template(
        "tela_depositarsaldo.html", saldo=ver_saldo())

@app.route("/tela_saquesaldo", methods=["GET", "POST"])
def tela_saquesaldo():
    erro = None
    if request.method == "POST":
        if not sacar(int(request.form["valor"])):
            erro = "Saldo insuficiente ❌"
        else:
            return redirect(url_for("tela_versaldo"))

    return render_template(
        "tela_saquesaldo.html",
        erro=erro, saldo=ver_saldo())

@app.route("/patrocinadores")
def patrocinadores():
    return render_template("patrocinadores.html")