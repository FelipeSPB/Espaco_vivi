from Server import App,db
from flask import jsonify,request, render_template
from login import Login
import jwt


@App.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@App.route("/home", methods=["GET"])
def home():
    return render_template("principal.html")

@App.route("/login", methods=["GET", "POST"])
def logging():
    if request.method == 'POST':
        login = request.form['login']
        senha = request.form['senha']
        verLog = Login.query.get(login)
        if verLog.senha == senha:
            return render_template("principal.html")
        else:
            return "Welp..."
    return render_template("login.html")


@App.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    if request.method == 'POST':
        login = request.form['login']
        senha = request.form['senha']
        nome = request.form['nome']
        email = request.form['email']
        user = Login.query.all()
        Dados = []
        for v in user:
            Dados.append({"Login": v.login})
        for verificar in Dados:
            if login == verificar["Login"]:
                return "Login usado"
        BD = Login()
        BD.login = login
        BD.senha = senha
        BD.nome = nome
        BD.email = email
        db.session.add(BD)
        db.session.commit()
        return "Cadastro OK"
    return render_template("cadastro.html")


@App.route("/deletar", methods=["GET", "POST", "DELETE"])
def check():
    if request.method == 'POST':
        login = request.form['login']
        senha = request.form['senha']
        user = Login.query.get(login)
        if not user:
            return "Login not found "
        elif user.senha != senha:
            return "Senha errada"
        else:
            db.session.delete(user)
            db.session.commit()
            return "Usuário deletado"
    return render_template("cadastro.html")

@App.route("/consulta", methods=["GET"])
def Consultar():
    user = Login.query.all()
    Retorno = []
    Response = {"Status":"", "Dados":"", "Mensagem":""}
    for u in user:
        Retorno.append({"Login": u.login, "Nome": u.nome, "E-mail": u.email, "Senha": u.senha})
    Response["Dados"] = Retorno
    Response["Status"] = "Sucesso"
    Response["Mensagem"] = ""
    return jsonify(Response)    