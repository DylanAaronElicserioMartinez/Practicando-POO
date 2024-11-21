print(" ")

print("Dylan Aaron Elicserio Martínez 3°W #Control:1179")

print(" ")
class Calculadora():
    def __init__(self, num1, num2):
        self._num1=num1
        self._num2=num2

    def suma(self):
        resultado=self._num1 + self._num2
        print(f"El resultado de la suma es: {self._num1} + {self._num2}={resultado}")

    def resta(self):
        resultado=self._num1 - self._num2
        print(f"El resultado de la resta es: {self._num1} – {self._num2}={resultado}")

    def division(self):
        resultado=self._num1 // self._num2
        print(f"El resultado de la divisón es: {self._num1} // {self._num2}= {resultado}")

    def multiplicacion(self):
        resultado=self._num1 * self._num2
        print(f"El resultado de la multiplicación es: {self._num1} * {self._num2} = {resultado}")

operacion=Calculadora(10, 10)
operacion.suma()

operacion=Calculadora(20, 10)
operacion.resta()

operacion=Calculadora(100, 2)
operacion.division()

operacion=Calculadora(50, 2)
operacion.multiplicacion()