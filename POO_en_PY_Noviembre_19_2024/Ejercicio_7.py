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