class Poligono:
    def calcularArea(self):
        raise NotImplementedError("Se debe implementar el método en la subclase")

class Triangulo(Poligono):
    def __init__(self, base: float, altura: float):
        self.base = base
        self.altura = altura

    def calcularArea(self)->float:
        return (self.base * self.altura)/2

class Cuadrado(Poligono):
    def __init__(self, lado: float):
        self.lado= lado

    def calcularArea(self)->float:
        return self.lado * self.lado

class Rectangulo(Poligono):
    def __init__(self, lado: float, altura: float):
        self.lado = lado
        self.altura = altura

    def calcularArea(self)->float:
        return self.lado * self.altura

def printArea(poligono: Poligono) -> float:
    return poligono.calcularArea()

def imprimirPoligonos():
    print("Área del Triángulo: ", printArea(Triangulo(3.3, 5)))
    print("Área del Cuadrado: ", printArea(Cuadrado(4.2)))
    print("Área del Rectángulo: ", printArea(Rectangulo(4.1, 6)))