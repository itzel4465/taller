from bottle import route, run, template

@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)
"""
@route('/')
def hola():
    return template('<b>Hello world</b>!', name=name)
"""
run(host='localhost', port=8080)