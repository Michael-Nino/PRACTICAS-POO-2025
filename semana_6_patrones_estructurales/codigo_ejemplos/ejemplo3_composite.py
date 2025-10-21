"""
EJEMPLO 3: Composite en Python
(Version cruzada del ejemplo C++ del PDF - Semana 6)
"""


class Figura:
    def dibujar(self):
        pass


class Circulo(Figura):
    def dibujar(self):
        print("Circulo")


class Grupo(Figura):
    def __init__(self):
        self.figuras = []
    
    def add(self, f):
        self.figuras.append(f)
    
    def dibujar(self):
        for f in self.figuras:
            f.dibujar()


c1 = Circulo()
c2 = Circulo()
g = Grupo()
g.add(c1)
g.add(c2)
g.dibujar()
