"""
EJEMPLO 2: Decorator en Python
(Ejemplo del PDF - Semana 6)
"""


def log(func):
    def envoltura(*args, **kwargs):
        print("Ejecutando funcion:", func.__name__)
        return func(*args, **kwargs)
    return envoltura


@log
def saludar(nombre):
    return f"Hola {nombre}"


print(saludar("Aldo"))
