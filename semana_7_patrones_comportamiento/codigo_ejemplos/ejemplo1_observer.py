"""
EJEMPLO 1: Observer en Python
(Ejemplo del PDF - Semana 7)
"""


class Observador:
    def actualizar(self, mensaje):
        print("Notificado:", mensaje)


class Sujeto:
    def __init__(self):
        self.obs = []
    
    def registrar(self, o):
        self.obs.append(o)
    
    def notificar(self, mensaje):
        for o in self.obs:
            o.actualizar(mensaje)


s = Sujeto()
o1, o2 = Observador(), Observador()
s.registrar(o1)
s.registrar(o2)
s.notificar("Se actualizo el sistema.")
