"""
DESARROLLO 2: Strategy para algoritmos de ordenamiento
(EJERCICIO NUEVO - NO es el ejemplo del PDF)
"""


class Ordenamiento:
    def ordenar(self, lista):
        pass


class Burbuja(Ordenamiento):
    def ordenar(self, lista):
        arr = lista.copy()
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr


class QuickSort(Ordenamiento):
    def ordenar(self, lista):
        if len(lista) <= 1:
            return lista
        pivote = lista[len(lista) // 2]
        izq = [x for x in lista if x < pivote]
        medio = [x for x in lista if x == pivote]
        der = [x for x in lista if x > pivote]
        return self.ordenar(izq) + medio + self.ordenar(der)


class Ordenador:
    def __init__(self, estrategia):
        self.estrategia = estrategia
    
    def ordenar(self, lista):
        return self.estrategia.ordenar(lista)


numeros = [64, 34, 25, 12, 22, 11, 90]
print("Original:", numeros)

ord1 = Ordenador(Burbuja())
print("Burbuja:", ord1.ordenar(numeros))

ord2 = Ordenador(QuickSort())
print("QuickSort:", ord2.ordenar(numeros))
