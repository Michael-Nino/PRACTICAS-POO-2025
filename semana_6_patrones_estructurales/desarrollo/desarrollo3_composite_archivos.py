"""
DESARROLLO 3: Composite para carpetas y archivos
(EJERCICIO NUEVO - NO es el ejemplo del PDF)
"""


class Elemento:
    def mostrar(self, nivel=0):
        pass


class Archivo(Elemento):
    def __init__(self, nombre):
        self.nombre = nombre
    
    def mostrar(self, nivel=0):
        print("  " * nivel + f"- {self.nombre}")


class Carpeta(Elemento):
    def __init__(self, nombre):
        self.nombre = nombre
        self.elementos = []
    
    def agregar(self, elemento):
        self.elementos.append(elemento)
    
    def mostrar(self, nivel=0):
        print("  " * nivel + f"/ {self.nombre}/")
        for e in self.elementos:
            e.mostrar(nivel + 1)


raiz = Carpeta("Documentos")
raiz.agregar(Archivo("informe.pdf"))

carpeta_imagenes = Carpeta("Imagenes")
carpeta_imagenes.agregar(Archivo("foto1.jpg"))
carpeta_imagenes.agregar(Archivo("foto2.jpg"))

raiz.agregar(carpeta_imagenes)
raiz.mostrar()
