from bottle import route, run, template


@route('/')
def hola():
    return template('<b>Hello world</b>!')

run(host='localhost', port=8080)