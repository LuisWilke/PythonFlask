from flask import Flask, url_for, render_template

# Initialize
app = Flask(__name__)

# routes
@app.route('/')
def ola_mundo():
    titulo = "Gestão de usuários"
    usuarios = [
        {"nome": "Guilherme", "membro_ativo": True},
        {"nome": "Joao", "membro_ativo": False},
        {"nome": "Luis", "membro_ativo": False},
    ]
    return render_template("index.html", titulo=titulo, usuarios=usuarios)

@app.route('/sobre')
def pagina_sobre():
    return """
    <b>ProgramadorPython<b>: asssista os videos no 
    <a href="https://youtube.com/@programadorpython">Canal no Youtube</a>
    """


# execution
app.run(debug=True)