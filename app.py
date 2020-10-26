from flask import Flask, request, jsonify
from Operaciones import Operaciones
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/suma', methods=['POST'])
def sumar():

    return 'Suma' 

@app.route('/resta', methods=['POST'])
def restar():

    return 'Resta' 

@app.route('/multiplicacion', methods=['POST'])
def multiplicar():

    return 'Multi' 
   

@app.route('/division', methods=['POST'])
def dividir():

    return 'Divi' 

if __name__ == "__main__":
	app.run(threaded = True,port = 3000, debug = True)