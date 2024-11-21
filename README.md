# Practicando-POO
Actividad en clase

#Codigo 1

print(" ")

print("Dylan Aaron Elicserio Martínez 3°W #Control:1179")

print(" ")

class Estudiante():

    def __init__(self , nombre , nota):
    
        self.nombre=nombre
        
        self.nota=nota
        
    def imprimir(self):
    
        print(f"Nombre:{self.nombre} \nNota: {self.nota}")

    def resultados(self):
    
        if self.nota >= 7:
        
            print("Has APROBADO!")
            
        else:
        
            print("Has REPROBADO!2")

estudiante1=Estudiante("Alfavix" , 9)

estudiante1.imprimir()

estudiante1.resultados()

estudiante2=Estudiante("Fin" , 10)

estudiante2.imprimir()

estudiante2.resultados()

![image](https://github.com/user-attachments/assets/252943ca-8396-45f8-9efe-f45b9af0f883)

![image](https://github.com/user-attachments/assets/c5fe53a1-d456-4b0b-96f6-abcbc73bfa77)

#Codigo 2

print(" ")

print("Dylan Aaron Elicserio Martínez 3°W #Control:1179")

print(" ")

class Persona:

  def __init__(self, n, e):
  
    self.nombre = n
    
    self.edad = e

  def cumpleaños(self):
  
    self.edad += 1

p=Persona(input("Ingrese nombre: "),int(input("Ingrese edad: ")))

p.cumpleaños()

p.cumpleaños()

print(f"{p.nombre} cumple {p.edad} años")

![image](https://github.com/user-attachments/assets/0522386e-6979-4986-8f2e-962d6c59480e)

![image](https://github.com/user-attachments/assets/9719a748-4530-423c-aa24-94a5cecf0d73)

#Codigo 3

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

![image](https://github.com/user-attachments/assets/d1a99083-63a5-4c82-b097-b3ba592fdd86)

![image](https://github.com/user-attachments/assets/0ebe68d6-3cde-479b-ad8c-e073d7e4126d)

#Codigo 4

print(" ")

print("Dylan Aaron Elicserio Martínez 3°W #Control:1179")

print(" ")

class Persona():

  def __init__(self,nom,ape):
  
    self.nombre=nom
    
    self.apellido=ape

  def nombre_completo(self):
  
    print(self.nombre + self.apellido)

class Estudiante(Persona):

  def __init__(self,nom,ape,carr):
  
    super().__init__(nom,ape)
    
    self.carrera=carr

  def mostrar_carrera(self):
  
    print(self.carrera)

  ![image](https://github.com/user-attachments/assets/06bea279-0ebc-43f5-9fc5-847bddb0a6eb)

  ![image](https://github.com/user-attachments/assets/edb02ad0-b879-4220-828c-3ea51717b5e9)

  #Codigo 5

print(" ")

print("Dylan Aaron Elicserio Martínez 3°W #Control:1179")

print(" ")

class Fabrica():

  def __init__(self, llantas, color, precio):
  
    self._llantas=llantas
    
    self._color=color
    
    self._precio=precio

class Moto(Fabrica):

  def cantidad(self):
  
    print("La cantidad de llantas: {}\nEl color es: {}\nEl precio es: {}".format(self._llantas,self._color,self._precio))

class Carro(Fabrica):

  def cantidad(self):
  
    print("La cantidad de llantas: {}\nEl color es: {}\nEl precio es: {}".format(self._llantas,self._color,self._precio))

    print("OBJETO=motocros")


moto=Moto(2, "Gris", "$200")

moto.cantidad()

print("OBJETO=Transformer")

carro=Carro(4 ,"Negro", "$600")

carro.cantidad()

![image](https://github.com/user-attachments/assets/db751752-1ed4-42e5-86d3-5b62e3a2af51)

![image](https://github.com/user-attachments/assets/aa73eea6-29b1-48a8-a68b-63ba8ea6b0a3)

#Codigo 6

print(" ")

print("Dylan Aaron Elicserio Martínez 3°W #Control:1179")

print(" ")

class Marino():

  def hablar(self):
  
    print("Hola soy un animal marino!")

class Pulpo(Marino):

  def hablar(self):
  
    print("Hola soy un pulpo!")

class Foca(Marino):

  def hablar(self,mensaje):
  
    self.mensaje=mensaje
    
    print(mensaje)

marino=Marino()

marino.hablar()

pulpo=Pulpo()

pulpo.hablar()

foca=Foca()

foca.hablar("Hola soy una foca!")

![image](https://github.com/user-attachments/assets/b66b3800-4b66-4331-8c85-4e4a4d4a07a3)

![image](https://github.com/user-attachments/assets/85460339-78b3-4555-ac77-80e04ed51cea)

#Codigo 7

print(" ")

print("Dylan Aaron Elicserio Martínez 3°W #Control:1179")

print(" ")

class Universidad():

  def __init__(self,Nombre):
  
    self.Nombre=Nombre

class Carerra():

  def carrera(self,especialidad):
  
    self.especialidad=especialidad

class Estudiante(Universidad,Carerra):

  def datos(self,nombre,edad):
  
    self.nombre=nombre
    
    self.edad=edad
    
    print(f"El nombre del estudiante es {self.nombre}, tiene {self.edad} , su especialidad es {self.especialidad}. Estudia en la Prepa {self.Nombre}")

persona=Estudiante("Cbtis128")

persona.carrera("Ingeniería mecatronica")

persona.datos("yuko", "8 meses de edad")

![image](https://github.com/user-attachments/assets/040df215-0632-4570-ae8d-93b0fd58d088)

![image](https://github.com/user-attachments/assets/b6008c21-0fa0-47ef-9a79-92690bbc0341)

