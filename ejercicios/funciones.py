def hola(nombre="Mundo"):
    print ("hola",nombre)

hola("itzel")
hola()

class Animal:
    def __init__(self, patas = 4, tipo = "pequeño"):
        self.patas = patas
        self.tipo = tipo

class Perro(Animal):
    def __init__(self, nombre = "Oddy", raza = "jack"):
        self.nombre = nombre
        self.raza = raza

    #def saludo(self):
        #return "Te saluda %s" % self.nombre

perrito = Perro (nombre="Peich", raza="shar pei")
perrito_juan = Perro()
print(perrito.nombre)
print(perrito.raza)
#print(perrito.tipo)
#print(perrito.patas)
#perrito.saludo
print(perrito_juan.nombre)
print(perrito_juan.raza)
#perrito_juan.saludo