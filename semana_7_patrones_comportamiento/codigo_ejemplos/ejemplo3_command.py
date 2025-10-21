"""
EJEMPLO 3: Command en Python
(Ejemplo del PDF - Semana 7)
"""


class Command:
    def ejecutar(self):
        pass


class ImprimirCommand(Command):
    def ejecutar(self):
        print("Imprimiendo documento...")


class GuardarCommand(Command):
    def ejecutar(self):
        print("Guardando documento...")


class Invocador:
    def __init__(self):
        self.historial = []
    
    def ejecutar(self, comando):
        comando.ejecutar()
        self.historial.append(comando)


i = Invocador()
i.ejecutar(ImprimirCommand())
i.ejecutar(GuardarCommand())
