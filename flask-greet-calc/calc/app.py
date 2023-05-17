# Put your app in here.
from flask import Flask, request
from operations import add,sub,mult,div
app = Flask(__name__)

@app.route('/add')
def add_():
    '''Add a and b'''
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    res = add(a,b)
    return str(res)    

@app.route('/sub')
def sub_():
    '''Subtract a and b'''
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    res = sub(a,b)
    return str(res)

@app.route('/mult')
def mult_():
    '''Multiply a and b'''
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    res = mult(a,b)
    return str(res)

@app.route('/div')
def div_():
    '''Divide a and b'''
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    res = div(a,b)
    return str(res)

##########################################################################################################################################

operations = {"add": add, "sub" : sub, "mult": mult, "div": div}

@app.route('/math/<oper>')
def math(oper):
    '''Combine all math operations into one page'''
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    res = operations[oper](a,b)
    return str(res)