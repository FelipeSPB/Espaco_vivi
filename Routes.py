from Server import App,db
from flask import jsonify,request, render_template
from login import Login

@App.route("/login", methods=["GET"])
def logging():
    return render_template("login.html")

@App.route("/login", methods=["POST"])
def logando():
    login = request.form['login']
    senha = request.form['senha']
    verLog = Login.query.get(login)
    verPass = Login.query.get(senha)
    if not verLog and verPass:
        return "Não cadastrado"
    else:
        return "Sussexo"

@App.route("/cadastro", methods=["GET"])
def cadastro():
    return render_template("cadastro.html")


@App.route("/cadastro", methods=["POST"])
def cadastrando():
    login = request.form['login']
    senha = request.form['senha']
    verLog = Login.query.get(login)
    verPass =  Login.query.get(senha)
    if not verLog:
        p = Login()
        p.login = login
        p.senha = senha
        db.session.add(p)
        db.session.commit()
        return "cadastrado"
    else:
            return "Erro"

@App.route("/deletar", methods=["GET"])
def check():
    return render_template("cadastro.html")

@App.route("/deletar", methods=["DELETE"])
def deletar():
    login = str(request.form['login'])
    senha = str(request.form['senha'])
    verLog = Login.query.get(login)
    verPass =  Login.query.get(senha)
    
    if not verLog:
        return "erro"
    elif not verPass:
        return "erro"
    else:
        p = Login()
        p.login = login
        p.senha = senha
    
        db.session.delete(p)
        db.session.commit()
        return "Usuário deletado"

@App.route("/consulta", methods=["GET"])
def Consultar():
    user = Login.query.all()
    return str(keepo)
    