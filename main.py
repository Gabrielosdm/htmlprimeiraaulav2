from flask import Flask, request
#objeto Flask

app = Flask(__name__)

#rota para /
@app.route('/')
def principal():
    return '<html>' \
           '<head>' \
           '<title>Página Inicial</title>' \
           '<style>' \
           '        h1{font-family:arial;' \
           '               font-size:52pt;' \
           '</style>' \
           '</head>' \
           '<body>' \
           '<h1><a href= ''/nome''>Nome</a>' \
           '<h1><a href=''/exibir?nome=Joao&sobrenome=Silva''>Exibir</a>' \
           '</body>' \
           '</html>' \





#rota para /nome
@app.route('/nome')

def nome():
     return 'Gabriel Pereia'

#rota para /exibir

@app.route('/exibir')
def exibir():
        nome = request .args . get('nome',default='Teste')
        sobrenome = request.args.get('sobrenome',default='Sobrenome')
        return nome + ' ' + sobrenome


#iniciar a app
if __name__ == '__main__':
    app.run(debug=True)