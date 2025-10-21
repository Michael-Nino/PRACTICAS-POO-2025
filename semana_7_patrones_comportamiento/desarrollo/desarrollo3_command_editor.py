"""
DESARROLLO 3: Command para editor de texto con guardar y deshacer
(EJERCICIO NUEVO - NO es el ejemplo del PDF)
"""


class Command:
    def ejecutar(self):
        pass
    
    def deshacer(self):
        pass


class GuardarCommand(Command):
    def __init__(self, editor):
        self.editor = editor
        self.backup = ""
    
    def ejecutar(self):
        self.backup = self.editor.contenido
        print(f"Guardado: {self.editor.contenido}")
    
    def deshacer(self):
        self.editor.contenido = self.backup
        print(f"Restaurado: {self.editor.contenido}")


class EscribirCommand(Command):
    def __init__(self, editor, texto):
        self.editor = editor
        self.texto = texto
        self.backup = ""
    
    def ejecutar(self):
        self.backup = self.editor.contenido
        self.editor.contenido += self.texto
        print(f"Escrito: {self.texto}")
    
    def deshacer(self):
        self.editor.contenido = self.backup
        print(f"Deshecho")


class Editor:
    def __init__(self):
        self.contenido = ""
        self.historial = []
    
    def ejecutar(self, comando):
        comando.ejecutar()
        self.historial.append(comando)
    
    def deshacer(self):
        if self.historial:
            comando = self.historial.pop()
            comando.deshacer()


editor = Editor()
editor.ejecutar(EscribirCommand(editor, "Hola "))
editor.ejecutar(EscribirCommand(editor, "Mundo"))
print("Contenido:", editor.contenido)
editor.deshacer()
print("Despues de deshacer:", editor.contenido)
