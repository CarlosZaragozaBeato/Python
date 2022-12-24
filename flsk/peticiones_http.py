from flask import Flask, request

app = Flask(__name__)

@app.route("/info", methods=['GET','POST'])
def inicio():
    cad = "<p>"
    cad = f"URL :{request.url} </br>"
    cad += f"PATH:{request.path} </br>"
    cad += f"Metodo: {request.method} </br>"
    cad += f"header: </br>"
    for item, value in request.headers.items():
        cad += f"{item}:{value} </br>"
    cad += "informacion en URL (GET): </br>"    
    
    for item, value in request.args.items():
        cad += f"{item}:{value} </br>"
    
    for item, value in request.files.items():
        cad += f"{item}:{value} </br>"
    return cad


@app.route("/suma", methods=["GET","POST"])
def sumar():
    if request.method == "POST":
        num1 = request.form.get("num1")
        num2 = request.form.get("num2")
        return str(int(num1)+int(num2))
    else:
        return '''<form action="/suma" method="POST">
				<label>N1:</label>
				<input type="text" name="num1"/>
				<label>N2:</label>
				<input type="text" name="num2"/>
                <input type="submit"/>
				</form>'''

	
if __name__ == '__main__':
  		app.run('0.0.0.0',8080, debug=True)