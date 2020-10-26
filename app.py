from flask import Flask, request, jsonify
from Operaciones import Operaciones
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/suma', methods=['POST'])
def sumar():

    numero1 = request.form.get('numero1')
    numero2 = request.form.get('numero2')

    numeroUno = float(numero1)
    numeroDos = float(numero2)
    suma = numeroUno + numeroDos

    print(suma) 
    return str(suma)

@app.route('/resta', methods=['POST'])
def restar():

    numero1 = request.form.get('numero1')
    numero2 = request.form.get('numero2')

    numeroUno = float(numero1)
    numeroDos = float(numero2)
    resta = numeroUno - numeroDos

    print(suma) 
    return str(resta) 

@app.route('/multiplicacion', methods=['POST'])
def multiplicar():

    numero1 = request.form.get('numero1')
    numero2 = request.form.get('numero2')

    numeroUno = float(numero1)
    numeroDos = float(numero2)
    multi = numeroUno * numeroDos

    print(suma) 
    return str(multi) 
   

@app.route('/division', methods=['POST'])
def dividir():

    numero1 = request.form.get('numero1')
    numero2 = request.form.get('numero2')

    numeroUno = float(numero1)
    numeroDos = float(numero2)
    division = numeroUno / numeroDos

    print(suma) 
    return str(division)

if __name__ == "__main__":
	app.run(threaded = True,port = 3000, debug = True)