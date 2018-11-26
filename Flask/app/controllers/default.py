from app import app


@app.route("/index")
@app.route("/")
def index():
    return "Hello World!"


@app.route("/teste/<name>")
@app.route("/teste")
def teste(name=None):
    if name:
        return  "Olá, %s!"
    else:
        return "vai embora"


'''Utilizando os métodos POST e GET (é possivel filtrar de qual tipo será usado)'''
@app.route("/teste2/", methods=['GET'])
def teste2():
    return "oi"

'''
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
