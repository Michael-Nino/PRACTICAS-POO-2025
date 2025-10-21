# Ejemplo 2: Factory en Python (EXACTO DEL PDF)

class Transporte:
    def entregar(self):
        pass

class Camion(Transporte):
    def entregar(self):
        return "Entrega por carretera"

class Barco(Transporte):
    def entregar(self):
        return "Entrega por mar"

class Factory:
    @staticmethod
    def get_transporte(tipo):
        if tipo == "camion": return Camion()
        elif tipo == "barco": return Barco()

t = Factory.get_transporte("barco")
print(t.entregar())
