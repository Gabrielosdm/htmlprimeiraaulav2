# coding=utf-8
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
               '               font-size:38pt;' \
                '           color:green;' \
               '</style>' \
           '</head>' \
           '<body>' \
               '<h1>Calculadora</h1>' \
               '<form action="/resultado" method="get">' \
                   'Número 1:<br>' \
                   '<input type="text" name="numero1"><br>'  \
                   'Número 2:<br>' \
                   '<input type="text" name="numero2"><br>' \
                   '<br><input type="submit" value="Somar">' \
                   '<input type="submit" value="Multiplicar">' \
                   '<input type="submit" value="Subtrair">' \
                   '<input type="submit" value="Dividir">' \
               '</form>' \
           '    <img src="fotossite:1486564177-finance-finance-calculator_81497">' \
           '</body>' \
           '</html>' \

@app.route('/resultado')
def resultado():
        n1=int(request.args.get('numero1'))
        n2=int(request.args.get('numero2'))
        soma=str(n1+n2)
        return soma

#iniciar a app
if __name__ == '__main__':
    app.run(debug=True)