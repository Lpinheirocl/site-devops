from flask import Flask, url_for, render_template

# Inicializacao
app = Flask(__name__)

# rotas
@app.route("/")
def ola_mundo():
    titulo = "Gestão de Usuários"
    usuarios = [
        {"nome": "Lucas", "membro_ativo": True},
        {"nome": "Duque", "membro_ativo": False},
    ]
    return render_template('index.html', titulo=titulo, usuarios=usuarios)

@app.route("/sobre")
def pagina_sobre():
    return """
        <b>Progamodor Python</b>: Vamos la
        """
#execucao
app.run(debug=True)