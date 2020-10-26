from flask import Flask, request, jsonify
from Operaciones import Operaciones
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/operaciones', methods=['POST'])
def sumar():
    if request.method == 'POST':

        numero1 = request.form.get('numero_uno')
        numero2 = request.form.get('numero_dos')
        suma = Operaciones()
        suma.suma(numero1, numero2)

        return 'La suma es ', suma 

    return "Hola"    

if __name__ == "__main__":
	app.run(threaded = True,port = 3000, debug = True)