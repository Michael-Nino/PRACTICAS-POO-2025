"""
DESARROLLO 2: Decorator para validacion en funciones matematicas
(EJERCICIO NUEVO - NO es el ejemplo del PDF)
"""


def validar_positivo(func):
    def envoltura(n):
        if n < 0:
            return "Error: numero negativo"
        return func(n)
    return envoltura


@validar_positivo
def raiz_cuadrada(n):
    return f"Raiz de {n} = {n ** 0.5}"


print(raiz_cuadrada(16))
print(raiz_cuadrada(-4))
