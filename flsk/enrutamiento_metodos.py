from flask import Flask, request 

app = Flask(__name__)

@app.route('/')
def inicio():
    return '<h1>Pagina principal</h1>'

@app.route('/articulos')
def articulos():
    return '<h1>Lista Articulos<h1/>'


@app.route('/articulos/new', methods=["POST"])
def articulos_new():
    return 'Esta URL recibe informacion de un formulario con el metodo POST'

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        return '<p>HEMOS ACCEDIDO CON POST</p>'
    else:
        return '<p>HEMOS ACCEDIDO CON GET</p>'

        
if __name__ == '__main__':
  		app.run('0.0.0.0',8080, debug=True)