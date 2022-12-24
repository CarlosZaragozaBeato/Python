from flask import Flask
app = Flask(__name__)	

@app.route('/')
def hello_world():
    a="54"
    b=int(a)
    color = "color:red"
    return f"<h1 style={color}>HELLO WORLD</h1>"

@app.route('/pruebas')
def pruebas():
    color = "color:yellow"
    return f"<h2 style={color}>Pruebas</h2>"

@app.route("/articulos")
def articulos():
    return "<h1>Lista articulos</h2>"

@app.route("/articulos/<int:id>")
def mostrar_articulo(id):
    return "<p>vamos a mostrar el artiuloc con id:{}".format(id)


@app.route("/hello/")
@app.route("/hello/<string:nombre>")
@app.route("/hello/<string:nombre>/<int:edad>")
def hola(nombre = None, edad = None):
    if nombre and edad:
        return f"El nombre es {nombre}, y la edad es {edad}"
    elif nombre:
        return f"El nombre es {nombre}"
    else: return "Hola mundo"


if __name__ == '__main__':
  		app.run('0.0.0.0',8080, debug=True)