from flask import Flask, make_response, abort, redirect,url_for

app = Flask(__name__)

@app.route('/string/')
def return_string():
    return 'Hello World'

@app.route('/object/')
def return_object():
    header = {'Content-Type':'text/plain'}
    return make_response('Hello, World',200,header)

@app.route('/login')
def login():
    abort(401)

@app.errorhandler(404)
def page_not_found(error):
    return 'Pagina no encotrada...',404

@app.route('/')
def index():
    return redirect(url_for('return_string'))

if __name__ == '__main__':
  		app.run('0.0.0.0',8080, debug=True)