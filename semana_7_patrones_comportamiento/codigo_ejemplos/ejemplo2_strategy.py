"""
EJEMPLO 2: Strategy en Python
(Version cruzada del ejemplo C++ del PDF - Semana 7)
"""


class Estrategia:
    def ejecutar(self):
        pass


class EstrategiaA(Estrategia):
    def ejecutar(self):
        print("Algoritmo A")


class EstrategiaB(Estrategia):
    def ejecutar(self):
        print("Algoritmo B")


class Contexto:
    def __init__(self, estrategia):
        self.estrategia = estrategia
    
    def set_estrategia(self, estrategia):
        self.estrategia = estrategia
    
    def operar(self):
        self.estrategia.ejecutar()


a = EstrategiaA()
b = EstrategiaB()
ctx = Contexto(a)
ctx.operar()
ctx.set_estrategia(b)
ctx.operar()
