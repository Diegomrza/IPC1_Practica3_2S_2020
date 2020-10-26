from flask import Flask, request, jsonify
from Operaciones import Operaciones
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/suma', methods=['POST'])
def sumar():

    numero1 = request.form.get('numero1')
    numero2 = request.form.get('numero2')

    suma = numero1+numero2
    return suma 

@app.route('/resta', methods=['POST'])
def restar():

    numero1 = request.form.get('numero1')
    numero2 = request.form.get('numero2')

    resta = numero1-numero2
    return resta 

@app.route('/multiplicacion', methods=['POST'])
def multiplicar():

    numero1 = request.form.get('numero1')
    numero2 = request.form.get('numero2')

    multiplicacion = numero1*numero2

    return multiplicacion 
   

@app.route('/division', methods=['POST'])
def dividir():

    numero1 = request.form.get('numero1')
    numero2 = request.form.get('numero2')

    division = numero1/numero2
    
    return division 

if __name__ == "__main__":
	app.run(threaded = True,port = 3000, debug = True)