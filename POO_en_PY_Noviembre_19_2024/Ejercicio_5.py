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