from flask import Flask, render_template_string, request, redirect, session, url_for

app = Flask(__name__)
app.secret_key = "minha_chave_secreta"

# Usuário e senha fixos
USUARIO = "admin"
SENHA = "1234"

@app.route("/")
def home():
    return """
    <h1>Bem-vindo ao Sistema</h1>
    <a href='/login'>Fazer Login</a>
    """

@app.route("/login", methods=["GET", "POST"])
def login():
    erro = ""

    if request.method == "POST":
        usuario = request.form["usuario"]
        senha = request.form["senha"]

        if usuario == USUARIO and senha == SENHA:
            session["usuario"] = usuario
            return redirect(url_for("dashboard"))
        else:
            erro = "Usuário ou senha inválidos!"

    return render_template_string("""
        <h2>Login</h2>
        <form method="POST">
            Usuário: <input type="text" name="usuario"><br><br>
            Senha: <input type="password" name="senha"><br><br>
            <button type="submit">Entrar</button>
        </form>
        <p style="color:red;">{{ erro }}</p>
    """, erro=erro)

@app.route("/dashboard")
def dashboard():
    if "usuario" not in session:
        return redirect(url_for("login"))

    return f"""
    <h1>Área Restrita</h1>
    <p>Olá, {session['usuario']}!</p>
    <a href='/logout'>Sair</a>
    """

@app.route("/logout")
def logout():
    session.pop("usuario", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)