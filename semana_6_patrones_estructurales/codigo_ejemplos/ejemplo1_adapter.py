"""
EJEMPLO 1: Adapter en Python
(Ejemplo del PDF - Semana 6)
"""


class EnchufeEuropeo:
    def conectar(self):
        return "220V conectado"


class Adaptador:
    def __init__(self, enchufe):
        self.enchufe = enchufe
    
    def conectar(self):
        return f"Adaptado a 110V -> {self.enchufe.conectar()}"


e = EnchufeEuropeo()
a = Adaptador(e)
print(a.conectar())
