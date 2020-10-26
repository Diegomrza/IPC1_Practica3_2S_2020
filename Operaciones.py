class Operaciones:

    def __init__(self):
        return None

    def suma(self, numero1, numero2):
        suma = numero1+numero2

        return suma

    def resta(self, numero1, numero2):
        resta = numero1-numero2
        return resta

    def multiplicacion(self, numero1, numero2):
        multiplicacion = numero1*numero2
        return multiplicacion

    def division(self, numero1, numero2):
        if numero2 != 0:
            division = numero1/numero2
            return division
        return 'No se puede dividir dentro de 0'    

    def potencia(self, numero1, numero2):
        print('Se hace lo que se puede D:')   

    def raiz(self, numero1, numero2):
        print('Lo de arriba')     