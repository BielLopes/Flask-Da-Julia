from app import app
from flask import render_template

from app.models.forms import loginFrom


@app.route("/index/<user>")
@app.route("/", defaults={"user":None})
def index(user):
    return render_template('index.html',
                            user=user)

@app.route("/login", methods=["GET", "POST"])
def login():
    form_login = loginFrom()
    if form_login.validate_on_submit():
        print(form_login.pasword.data)
        print(form_login.username.data)
    else:
        print(form_login.errors)
    return render_template('login.html',
                            form_login=form_login)
'''
    """
    <html>
        <head>
            <title>Hello World!</title>
        </head>
        <body>
            <h1>Hello World!</h1>
            <h2>Isto é uma string em block</h2>
        </body>
    </html>
    """

'''



'''
@app.route("/teste/<name>")
@app.route("/teste")
def teste(name=None):
    if name:
        return  "Olá, %s!"
    else:
        return "vai embora"


Utilizando os métodos POST e GET (é possivel filtrar de qual tipo será usado)
@app.route("/teste2/", methods=['GET'])
def teste2():
    return "oi"


Comessando a entender tipos na definiçãod de rotas
@app.route("/teste/<name>")
def teste(name=None):
    print(type(name))
    return ""
Agora Fazendo uma inferência de tipo, caso seja achado uma string retorna uma 404
Só existem o tipo int e o str que é por default
@app.route("/teste/<int:id>")
def teste(id):
    print(type(id))
    return ""
'''
